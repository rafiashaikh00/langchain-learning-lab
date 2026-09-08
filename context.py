from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
"""Contextual Compression Retriever is problem ko fix karta hai: ye pehle normal retrieval karta hai, phir har retrieved document ko "squeeze/compress" karta hai taake sirf query se directly relevant hissa reh jaye, baqi sab hata diya jaye."""

# Recreate the document objects from the previous data
docs = [
    Document(page_content="""The Grand Canyon is one of the most visited natural wonders in the world.
    Photosynthesis is the process by which green plants convert sunlight into energy.
    Millions of tourists travel to see it every year. The rocks date back millions of years.""",
             metadata={"source": "Doc1"}),

    Document(page_content="""In medieval Europe, castles were built primarily for defense.
    The chlorophyll in plant cells captures sunlight during photosynthesis.
    Knights wore armor made of metal. Siege weapons were often used to breach castle walls.""",
             metadata={"source": "Doc2"}),

    Document(page_content="""Basketball was invented by Dr. James Naismith in the late 19th century.
    It was originally played with a soccer ball and peach baskets. NBA is now a global league.""",
             metadata={"source": "Doc3"}),

    Document(page_content="""The history of cinema began in the late 1800s. Silent films were the earliest form.
    Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
    Modern filmmaking involves complex CGI and sound design.""",
             metadata={"source": "Doc4"}),
]

# Create a Chroma vector store from the documents
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    collection_name="compression_demo"
)
#ye normal Chroma retriever hai, jaisa aap pehle use kar chuke hain:
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# Set up the compressor using an LLM
llm = ChatOllama(model="gemma3:1b")
"""Internally ye ek LLM prompt use karta hai jo kuch aisa hota hai:

"Given this document and this question, extract only the parts of the document that are relevant to answering the question. If nothing is relevant, return nothing."

Har retrieved document is prompt ke through LLM ko jata hai, aur LLM sirf relevant text return karta hai."""
compressor = LLMChainExtractor.from_llm(llm)

# Create the contextual compression retriever
compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

# Query the retriever
query = "What is photosynthesis?"
"""Jab aap compression_retriever.invoke(query) call karte hain, internally ye process hota hai:

base_retriever.invoke(query) → 5 raw documents milte hain
Har document compressor se guzarta hai (LLM call, ek document ke liye ek call)
Compressed documents wapas milte hain — kuch documents completely empty/drop bhi ho sakte hain agar unmein kuch relevant na ho"""
"""Ek paragraph (chunk) mein kayi topics mix ho sakte hain — jaise 3 lines Topic A ki, 1 line Topic B ki. Jab aap Topic B ke baare mein query karte hain, to normal retriever pura paragraph wapas de deta hai (Topic A ki lines samet), kyunki vector search chunk-level pe kaam karta hai, sentence-level pe nahi — is liye chunk ka embedding thoda Topic B se milta hai to pura chunk retrieve ho jata hai, chahe usme zyada tar content unrelated ho. Contextual Compression Retriever isay do steps mein solve karta hai: pehle base_retriever normal tareeke se top-k relevant chunks dhundta hai (coarse filter — poore paragraphs, mixed content ke sath), phir har retrieved chunk ko ek compressor (LLMChainExtractor) ke through guzara jata hai jo us chunk ko LLM ko query ke sath deta hai aur bolta hai "sirf wo part nikaalo jo is query se directly relevant hai" — ye fine filter hai jo sentence-level pe kaam karta hai, matlab Topic A ki lines drop ho jati hain aur sirf Topic B wali line bachti hai. Agar kisi chunk mein query se bilkul kuch relevant na mile, to compressor us pure chunk ko discard kar deta hai, is liye final results mein kabhi retrieved-k se kam documents bhi mil sakte hain. Trade-off ye hai ke har chunk ke liye ek extra LLM call lagti hai compression ke liye, jisse process thora slow/costly ho jata hai, lekin final context clean aur precise milta hai — jo better RAG answers ke liye zaroori hota hai.

Write a message…


"""
compressed_results = compression_retriever.invoke(query)

for i, doc in enumerate(compressed_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
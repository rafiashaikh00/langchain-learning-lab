from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
#we can use this by chromadb but useing tririval we make cahisn and inplemnt adcance retreriver do advance seraching
#we import the Document class so we can create objects like:
"""
If we are working with LangChain Document objects, we import the Document class. A Document contains page_content and optional metadata. If we only need simple text and don't need the Document structure, we can use a normal list of strings. But when working with LangChain components such as document loaders, text splitters, and vector stores, we commonly work with Document objects, so we use Document."""
#So yes, object banate waqt Document(...) likhte hain, because Document is the class we're creating objects from.
Docs = [
    Document(
        page_content="""
        LangChain is a framework for building applications powered by large language models.
        It provides components such as prompts, models, document loaders, retrievers, vector stores,
        and output parsers. These components can be combined to build applications like chatbots,
        question-answering systems, and Retrieval-Augmented Generation applications.
        """
    ),

    Document(
        page_content="""
        Retrieval-Augmented Generation, commonly called RAG, combines information retrieval
        with a large language model. First, relevant documents are retrieved from a knowledge base.
        The retrieved documents are then provided to the language model as context so that it can
        generate an answer based on external information.
        """
    ),

    Document(
        page_content="""
        Vector databases store numerical representations of text called embeddings. An embedding
        model converts text into vectors that represent the semantic meaning of the text.
        A vector database such as Chroma can compare a query vector with document vectors and
        retrieve documents that are semantically similar to the query.
        """
    ),

    Document(
        page_content="""
        Text splitting is an important step in a RAG pipeline. Large documents are divided into
        smaller chunks before they are converted into embeddings. Chunk size and chunk overlap
        affect retrieval quality. Good chunking helps the retriever find focused and relevant
        pieces of information from a large document.
        """
    ),

    Document(
        page_content="""
        A retriever is responsible for finding relevant documents for a user query. Different
        retrievers can use different search mechanisms. A vector retriever uses embeddings and
        similarity search, while keyword-based retrievers use keywords and ranking algorithms.
        The retrieved documents can then be passed to an LLM to generate an answer.
        """
    )
]

#initilize krty hn embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#Docuemnt hn uper wo umara class hn docs obj hn chroma.from docuemnts ek method hn
#create chroma vector store in memory
#from_documents()  → Chroma ka method
#Document          → class
#mean from_docuemnts docs obj lega and embedding model se vector m convert kar ke chroma me store kare ga my collection ek tabel hn us ka dr store kare ga
#Chroma collection mein documents ke saath unke embeddings aur associated information bhi maintained hoti hai.
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma.from_documents(
    #documents=        → Chroma method ka parameter
    documents=Docs,
    embedding=embedding,
    collection_name='my_collection'
)
#earch_kwargs is a dictionary that contains search configuration/settings. k=2 tells the retriever to return the top 2 relevant documents for a query. It does not perform multiple searches.
#
#**kwargs ek mechanism hai jisse function multiple named/keyword arguments receive kar sakta ha
#hume basically vector store ko retriver me convert kare ge,as_retriever ko hum convert kare ge vectore store ko retriver m convert kare ge
retriever=vector_store.as_retriever(search_kwargs={"k":2})#Retriever ki search ke waqt k=2 use karo, yani mujhe top 2 relevant documents do."

#query
query='what is chroma used for?'
results=retriever.invoke(query)#retriver es query ko vector m convert kar ek semetic serach perform kare ga and giev top 2 result ans show to u and send to docuemnt obj formate then store to results

for i, doc in enumerate(results):

    print(f'\n----- Results {i+1} -----')

    print(f"Content:\n{doc.page_content}....")
#MMR retrieves documents that are relevant to the query while also avoiding documents that are too similar to each other 
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


docs = [
    Document(
        page_content="""
        LangChain is a framework for building applications with large language models.
        It provides components such as prompts, models, chains, retrievers, and tools.
        Developers can combine these components to create AI-powered applications.
        """
    ),

    Document(
        page_content="""
        LangChain provides many components that make LLM application development easier.
        Important components include prompt templates, chat models, output parsers,
        retrievers, and tools. These components can be connected together into workflows.
        """
    ),

    Document(
        page_content="""
        Prompt templates are a LangChain component used to create reusable prompts.
        Instead of writing the same prompt repeatedly, developers can define a template
        with variables and provide different values at runtime.
        """
    ),

    Document(
        page_content="""
        Retrievers are LangChain components responsible for finding relevant documents
        for a user query. A retriever can use vector similarity, keyword search, or
        another search mechanism to retrieve useful information from a knowledge base.
        """
    ),

    Document(
        page_content="""
        Tools allow an LLM application to interact with external systems and perform
        actions. A tool can represent functions such as searching the web, querying
        a database, calling an API, or performing a calculation.
        """
    )
]
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma.from_documents(
    #documents=        → Chroma method ka parameter
    documents=docs,
    embedding=embedding,
    collection_name='new'
)
#1 "Relevance ko maximum importance do; diversity ko almost ignore karo.",0 se diversitty zeyda ugei revelnce kam hugei 
retriever=vector_store.as_retriever(
    search_type='mmr',search_kwargs={"k":2,"lambda_mult":1})#lambda func use huga diversity and revelance kitni hu 0 se 1 tak huta hn 
query='what is Langchain?'
results=retriever.invoke(query)#retriver es query ko vector m convert kar ek semetic serach perform kare ga and giev top 2 result ans show to u and send to docuemnt obj formate then store to results

for i, doc in enumerate(results):

    print(f'\n----- Results {i+1} -----')

    print(f"Content:\n{doc.page_content}....")
    #chroma ka apna retrival technique huta hn wo enh sabh se algh hn kam wahi hn maghr ye retrival tooic chroma ka wala nhi hn ok
#indexing is a approach to find for usefull for seraching we do clsuters form what is cluster a group of similar vectors suppose we have 
#1 milloon vcetors ,abd clusyter a,b ,c ,d ese 4,5 group bane ge then unh k centriokd banyge whta is centriod per grioup ka 
# hum unh sare cluster l jo movies hn unh ka average neklay ge x ,y me se ek nya vector bane ga wo nya vector basically us cluster ko refrence dega hum apni query per cluster k centriod se compare krty hn

#chroma is lightweight it is vector database,its is mid in both sides stor + db
#1 is hierecacy is user in top , 2. can creat multiple databse,3. in one db you can create multiple tables ,4. table can store multiple metadata , and embeddings 

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

#creating 5 docuemnt object
from langchain_core.documents import Document

# Create LangChain documents for IPL players

doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and consistency, he has represented Royal Challengers Bengaluru throughout his IPL career.",
    metadata={"team": "Royal Challengers Bengaluru"}
)

doc2 = Document(
    page_content="Rohit Sharma is one of the most successful captains in IPL history, leading Mumbai Indians to five IPL titles. He is known for his calm leadership, excellent batting skills, and experience in T20 cricket.",
    metadata={"team": "Mumbai Indians"}
)

doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicket-keeping abilities, and leadership have made him one of the most respected players in IPL history.",
    metadata={"team": "Chennai Super Kings"}
)

doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his accurate yorkers, variations, and ability to perform under pressure.",
    metadata={"team": "Mumbai Indians"}
)

doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, he is known for his left-arm spin bowling, powerful batting, and excellent fielding skills.",
    metadata={"team": "Chennai Super Kings"}
)
#making list in which i put all the document
doc=[doc1,doc2,doc3,doc4,doc5]

#form vector store make object of chroma
vector_store=Chroma(
    #Kaunsa model vectors banayega?
    embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
    #humare jo vectors hn embeddings ke wo kis location m store kare ge,so here in root we make a folder chroma_db 
    persist_directory='chroma_db',#es ko run kare ge aghr folder nhi bana huwa to kudh es folder m ban jae ga
    #collection= table in db es me sare dicuments as table m jese store huth hn na huga
    collection_name='sample'
)

#this used to add docuemnts in 
#vector_store.add_documents(doc) hume ye ek bar run krna hn warna humare chroma me bar bar yhi docuemnt add hujae ga to comment krdo
# # es se ye huga ke us folder m sare embeddings add hugei also theit indexing too mean per docuemnt id generate hugei we can retrive the docuemnt by id
#es folder me per docuemnt ki id metadata ans embeddings huge embeddinmg me per doucment ke 384  numbers of vector taht store inside chroma folder
#to see all daat id ,metadata e,bediings
"""data = vector_store.get()

print(data)"""
#.get se fetch huegi data we can see sabh ko automatically id mily ge 5 embeiings huegi 5 meta data
"""a=vector_store.get(include=['embeddings','documents','metadata'])
print(a)"""


#hum similarty score be delkh sekhty hn kam score zeyda acha vector_store.similarity_search_with_score

#search
result=vector_store.similarity_search(
    query="who among these are a bowler?",
    # k ka matalb huta hn ap kitny similar objects ko dkehan cahahty hn numbers
    k=3
)
#print(result)

#meta-data ko filter krty hn jese kon 
result2=vector_store.similarity_search_with_score(
    #query ko khali rakhty hn
    query='',
    #mean wo filter hu kar ajae jo es team se belong krty hn
    filter={'team':"Chennai Super Kings"}
)
print(result2)

#hum update kese kare ge
"""update_doc1=Document(
    page_content="virat kholi has amazing beautifull wife",
    metadata={"team":"pakistan"}
)
#you have to provide old id here
vector_store.update_document(document_id='',document=update_doc1)
#delete priovide id
vector_store.delete(ids=[""])"""

#thsi is best way to laod everyonee by tehir ids 
data = vector_store.get(
    include=["documents", "metadatas"]
)

for id, document, metadata in zip(
    data["ids"],
    data["documents"],
    data["metadatas"]
):
    print("ID:", id)
    print("Document:", document)
    print("Metadata:", metadata)
    print("--------------------")


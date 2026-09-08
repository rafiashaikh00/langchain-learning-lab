#single embingings
"""from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings=OpenAIEmbeddings(model='',dimension=32)
result=embeddings.embed_query("what is capital of india")
#mean wo es code ko vector m cahneg akre ga and 32 dimensions more vvectore more achimeaning
print(str(result))
#this si multi embeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings=OpenAIEmbeddings(model='',dimension=32)
document=["Delhi is capital of which country","what is a flag"]
result=embeddings.embed_documents(document)
#mean wo es code ko vector m cahneg akre ga and 32 dimensions more vvectore more achimeaning
print(str(result))
"""
#chat model thinks and writes answers. An embedding model only converts text into numerical vectors that capture its meaning.pyt
#open source 
"""from langchain_huggingface import HuggingFaceEmbeddings
#call class kr rhy hn us k andr model name 
embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#input
text="Delhi is teh capital of india"
result=embedding.embed_query(text)
print(str(result))"""
#multiline
"""from langchain_huggingface import HuggingFaceEmbeddings
#call class kr rhy hn us k andr model name 
embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#input
document=["Delhi is capital of which country","what is a flag"]
result=embedding.embed_documents(document)
print(str(result))
print(len(result))
print(len(result[0]))"""
"""
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text1 = "hi"
text2 = "Rafia is studying at SZABIST in CS-6 and she loves learning about embeddings and machine learning"

result1 = embedding.embed_query(text1)
result2 = embedding.embed_query(text2)

print("Length for short text:", len(result1))
print("Length for long text:", len(result2))
#Length for short text: 384 kyu ke embedding quey hu ya doucment kya huga ek word prha token banaya temp vector bana 384 ese sare docuemnt ke per word ka huga in the end sare 384 sabh mila k ek avergae 384 mily ga kyu k ye model 384 support krta bara model aur zeyda vector dega and ek num se hum indetiuy nhi pae ge ye kis ko dnete kre ga
#Length for long text: 384"""

"""
1 query → 2D result me sirf 1 row hoti hai (shape (1,4)) → seedha [0] laga ke wo ek row nikal lete hain.
2+ queries → 2D result me utni hi rows hoti hain jitni queries (shape (n, 4)) → har row ek query ka result hoti hai (us query ka har doc ke saath score).
Isliye jab multiple queries ho, hum loop use karte hain — taake har row (har query) ko alag se process kar sakein.
Har row ke andar, hum phir se sorted + [0] use karte hain us specific query ke liye highest score wala doc dhundne ke liye."""



from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
documents = [
    "Virat Kohli is one of the greatest Indian batsmen.",
    "Jasprit Bumrah is India's leading fast bowler.",
    "MS Dhoni is a legendary captain and wicketkeeper.",
    "Rohit Sharma is the captain of the Indian cricket team."
]
#one query 4 documnt to hspe is 1:4
# User Query
query = "Tell me about best player in cricket"#cause it is one query to hum es ko 2D em store kare ge aghr twio query huti to hum es ko list m algh se store nhi krty

# Generate Embeddings humare pas jo word huta hn sabh ki ye model 384 vector gen kre ga last em jab senntence over huga to sabh 384 har word k vector ka vaerage nekla k hume 384  vector return krta hn
doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)
#humare pas query ek hn esliye ye ek serf line hn numbwr ki esliye hum esko list em daley ge ab ye grid ban gya of one row mena it now give shape of 2D and kyu k documnet k pas alreday 4 rows hn per row ek list ban of vector ban jae ge so hum es ko fir se kesi list m nhi daly ge its already 2 D
# Similarity Scores mean query vector ka jo vector hn us ko match akre ga 4 vector se and 0 ak matlab hn first row se start akro
scores = cosine_similarity([query_embedding], doc_embedding)[0] #0 cause i ahve one query if i ahvve multiple query no num write here
#enumerate mean index add akro  sabh me and 1 mean us ko index k bas pe nhi second part k base pe karo 
# Sort (Highest Similarity First)
#enumete score ko index ,value m convert kare ga tehn list bane gei then fucn chly ga score k basis pe asdending order flow huga docuemnt index se automaticlaly 0 jae ga print huga first if we want top 3 so [:3] use slice or u cahnge 0 se 2 second top most 
index, score = sorted(
    list(enumerate(scores)),
    key=lambda x: x[1],
    reverse=True
)[0]
# 0 ka matlab hn jo phla hn na descdending me obv wo score high uga us dicyemnt ak wo index to wo lien print hugei
print("Query:")
print(query)

print("\nMost Relevant Document:")
print(documents[index])

print("\nSimilarity Score:")
print(score)

from langchain_huggingface import HuggingFaceEmbeddings
from skllearn.metrics.pairwise import cosine_similarity
embedding=HuggingFace(model_name='')
document=["Virat Kohli is one of the greatest Indian batsmen.",
    "Jasprit Bumrah is India's leading fast bowler.",
    "MS Dhoni is a legendary captain and wicketkeeper.",
    "Rohit Sharma is the captain of the Indian cricket team."
]
query="who is Rohit Sharma"
doc_embedding=embedding.embed_documents(document)
query_embedding=embedding.embed_query(query)
scores=cosine_similarity([query_embedding],doc_embedding)[0]
index,score=sorted(list(enumerate(score)),key=lambda x:x[1],reverse=True)[0]


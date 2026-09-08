#pip install youtube-transcript-api
#hum youtube ki transcpit use kr ke kesi be video ke transcpit use kr sakhty as a string in our code
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
# ek walal trascipt loa kare ga dhusra exception ahndling kare ga
from langchain_text_splitters import RecursiveCharacterTextSplitter
#text ko chunks me divide kare ga
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_ollama import ChatOllama

from langchain_chroma import Chroma

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda
#step1 -> indexing mean content load
#indexing -> hum docuemnt ko load kar ke us kiembeddings gen kare ge
video_id='Gfr50f6ZBvo'#this is a id io get from url se 
try:
    # YouTube Transcript API ka object
    api = YouTubeTranscriptApi()

    # Video ki English transcript fetch karo
    transcript_list = api.fetch(
        video_id,
        languages=['en']
    )

    # Saare subtitle chunks ko ek single string mein convert karo
    #phly to jo be cheex join kare ge unh k bech m space huga and,.join sari strings ko space ke sath join kare ga
    #transcript_list ke andr sare itny chunks hn ok ab ek chunk nekla transcript_list me se wo ghya chunk variabkle me us pe chunk.text operyion perform huwa and ab text nekla print huwa then again new chunk transcript_list se nekla wo gya chunk varaible em us pe opertion huwa chunk.text ka
    transcript = " ".join(
        chunk.text for chunk in transcript_list
    )

    #print(transcript)

#Ek-ek chunk chunk variable mein aata hai → chunk.text se uska text nikalta hai → next chunk aata hai → same operation hota hai → saare texts ko " ".join() spaces ke saath ek single string mein combine kar deta hai."""

except TranscriptsDisabled:
    print("Transcript is disabled for this video.")

#ab jo hume pora transcript mila hn 2 hr ki video ka us ko chunsk m divide kare ge
splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    #per sentences 1000 chracters
    chunk_overlap=200
    #new sentetnces old char repeat
)
#step 2 text splitting
#jo transcript humare pas hn us ko splitter waly rules me break kare and then make document objects and store in a list
chunks=splitter.create_documents([transcript])
"""print(len(chunks),"length of chunks")168 chunks exit krty hn
print("zero chunk hn ye",chunks[0])"""

#step->3 embeddings,vector store  chroma
embeddings= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store=Chroma.from_documents(

    documents=chunks,
    embedding=embeddings,
    collection_name='my_tutorial'
)#data vectore_store me hn hum es ko get method use kre ge shwo krni hn embeddiings and docuemnt 
#vectore store k andr actually chroma ka object hn us ke andr embeddings hn ab .get se se hume two cheeze cahhye
#include se konsi info chhaye
data = vector_store.get(
    #as im using chroma us m field huti hn documenst ,embeddings, ese if m dhusri databse ixe kro us ki field cahneg hugei
    include=["embeddings", "documents"]
)
"""data dict ke andr konsi varaibles hn jese id metadata docuemnt ,embeddings ese"""

#print(data.keys())

#print("First chunk:")
#print(data["documents"][0])

#print("First embedding:")
#print(data["embeddings"][0])

"""Here indexing is over jis me docuemnt load,text split , store in vector database, embeddings bani ab next step"""
"""Stage 2 RETRIVAL """
#hum apny vectore store k andr jo chroma obj hn us ko retrival m
#ye muje convert krta hn retriver me as retriver and serach es ka simialr vector hu and top 3 de
retriever=vector_store.as_retriever(search_type='similarity',search_kwargs={'k':5})
## retriever ke output me relevant Document objects milte hain
# in Document objects ke andar page_content hota hai
# embeddings retrieval/search ke liye vector store me use hoti hain

# we send our query to retriver 
"""query='what is deepmind'
result=retriever.invoke(query)"""
# # first retriver es query ko  embddings em convert krta hn and result me store kare ga tehn query k accoording uper wali cheeze jkare ga
#dekho abi tak humen model use nhi kya huamre pas exiting chunk jio be humare query rea;ted hn wo as it is hume mily ge by retriver but aghr yha llm huta to docuemnt ko prh k kudh se ek jawab deta undesttand
#print(result) # you will get top 3 

"""Stage 3 augmentation where we make  promp tempalte query and xontext ko mila ke hum prompt bane ge """

prompt = PromptTemplate(
    template="""You are a helpful AI assistant.

Answer the question using ONLY the information given in the transcript context.

Rules:

1. Do not use your own knowledge.
2. Do not make up information.
3. Give a short and clear answer.
4. If the answer is not found in the context, say: "I don't know based on the provided transcript.".
5.Answer should be from above things and correct answer give me i trust you "

Transcript Context:
{context}

Question:
{question}

Answer:""",
    input_variables=["context", "question"]
)
#question='is thsi video discuss about aliens? if yes then what was discussed?'
#yha per be question  k embeddings ban jae gei tehn wo check kare ag most reveralnt kosne documnt hn query k hesab se
"""retriver_docs=retriver.invoke(question)"""
#sare  wo 4 document ek ek kar k doc m jae ge maghr bas unh k page content sabh aaghy then join hugae with 2 new lines se
"""context_text='\n\n.join(doc.page_conetnt for doc in retriver_docs)'#yha se wo  top 3 docuemnt k page conetnt jae ge"""
"""final_prompt=prompt.invoke({'context':context_text,'question':question})# fianl promot me 3 documnt be jae ge ans also quetion be hn"""
"""answer=model.invoke(final_prompt)
print(answer.content)"""
question ="Can you summarize the video and also highlight the key points step by step?"#ques
#retrieved_docs = retriever.invoke(question)# question ko embeddimg m convert kr k top 3 docuemnt mily
#hum es cheex ko commnet out esliye kare ge kyu k ye manul process hn neeceh cahin se kare ge
# Step 5: Augmentation (Combine Context)
#context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)# wo sare top 3 document ek ek kar k doc m gae an pagecoentnt nekla sabh ka
#step 6 Generation
model=ChatOllama(model="gemma3:1b",temperature=0.2)
#final_prompt = prompt.invoke({'context': context_text, 'question': question})# dono cheexe fill  hui final prompt m
#response = model.invoke(final_prompt)#final prompt model ko hit kya

#print("--- Model Response ---")
#print(response.content)
# ----- CHAIN FORMATION STAGE 7
# ek fun bane ge context ka
#yha retriced doc ek varaibek hn uoer walal obj nhi wo comment out hn
def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text
"""Chroma ke andar: id + embedding + document + metadata
Retriever ka output: relevant Document objects
Document object mein: page_content + metadata
Embedding: retrieval/search ke liye Chroma/vector store mein use hoti hai; retrieved Document ka normal part nahi hoti.

Tumhari last line ko correct karke:

Retriever question ki embedding ko Chroma mein stored embeddings ke saath compare karta hai, matching records ke corresponding Document objects retrieve karta hai. Phir ye Document objects format_docs ko milte hain."""
parallel_chains=RunnableParallel(
    #hum  es func ko runnabel em convert krn ahuga tabh chain m aae ga
    # invoke se question gya question se retriver n 5 dicyument bhjy then format doc  k andr paarmeter n receive kiye fir contect bana
    {'context':retriever|RunnableLambda(format_docs),
    'question':RunnablePassthrough()
    }
)

parser=StrOutputParser()
main_chain=parallel_chains|prompt|model|parser
result=main_chain.invoke(question)
print(result)
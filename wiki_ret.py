#retriver is like a fucn which input me takes user query and then it go to datyabase serach for query then find revelant documents and fetch teh docuemnts and show it to you
#all retrivers are runnables so we make chains
#diff data sources have diff retriver 1. wekipidia retriver so data wikipidia se aake ge 2, vector databsse, 3. R drive 
#A retriever's job is simply: find revelant ans and show to you it doesnot generate any ans

#query go to wikipidia retriver it go to api of wikipidia where it found most revelant document about query and send most top 2 document and send to you so basically api of wikipidia find doucmnt
#code

from langchain_community.retrievers import WikipediaRetriever
#oject , top k result wo show krta hn top k kitny result cahhye , langyuage konsi hu 
retriever=WikipediaRetriever(top_k_results=2,lang='en')
#query 
query="Pakistan India relations"
#
docs=retriever.invoke(query)
print(docs)


#print retrived content by loop
#docs ke andr jo hn uski indexing kro index ko i ke pas bhjo and docuemnt  ko doc ke pas and result (i+1) mean start from result 0+1=1 se and doc ke pas docuemnt hn na us ak .pageconetnt dekhao bas
for i, doc in enumerate(docs):

    print(f'\n----- Results {i+1} -----')

    print(f"Content:\n{doc.page_content}....")
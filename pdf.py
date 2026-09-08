#ye hn koi esa pdf jis m images ya wo scaanend na huwato
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('rag/coffee.pdf')
docs=loader.load()
print(docs)
#this is for ek folder ke andr pdf load kr rhy hu

#TextLoader poore file ka text ek hi single Document object mein daal deta hai (ek list jisme sirf 1 element hota hai).
#PyPDFLoader har page ka alag Document object banata hai, toh list mein utne elements hote hain jitne pages — aur har element ke andar metadata mein page number hota hai.
#TextLoader → 1 file = 1 Document object → list mein sirf 1 element
#PyPDFLoader → 1 file lekin N pages = N Document objects → list mein N elements (ek document object per page)
##docs[0] → page 1 ka content (kyunki 0-indexed hai)
#docs[1] → page 2 ka content
#docs[n] → page (n+1) ka content
print(docs[0].page_content)#first page 
print(docs[1].page_content,"this is second page content") #second page
print(len(docs)) #page 0 is index and pagelabel is current oage numer
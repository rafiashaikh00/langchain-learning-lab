from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
#actually ye kya krta hn ke ek folder ko memory me load krta hn and us ke andr jo text files hn ya pdf csv ya any other types ap sah data ko sath m read kr pae ge
loader=DirectoryLoader(
    path='rag/check',
    #kis pattern wali hume files chahye like all text files,all pdf files, csv , ya any types
    glob='*.pdf',
    #as all files are pdf we use pdf class if there is text files we use text , if csv we use csv 
    loader_cls=PyPDFLoader
#directoryloader ek folder ko lpoad kare ga then pdf walal har document ka algh se obj banane ga utny sabh ek list m store huge


)
#if i used laxy_load us se ye huga ke fast doucment ,load hueg mean ek ,load huga fir wo meemory se chla jae ga fir next aae ga ese so on memory m load sab ek sath nhi huge aghr huwe to slow huga ans lazyload se ek docuemnt load huga fir wo chla jae ga hum apny opertion kr lege then next aae ga no s,low
docs=loader.load()
print(len(docs)) # es se sare pages on all the files jis k type pdf hn us k sare pages ka num btae ga collectively
print(docs[2].page_content)
#this way to find like in a list of docs load in doc one by one then check if meta data ke source me coffe hn to print kro us ke page label
for doc in docs:
    if 'coffee' in doc.metadata['source']:
        print("Coffee page:", doc.metadata['page_label'])
    elif 'space' in doc.metadata['source']:
        print("Space page:", doc.metadata['page_label'])
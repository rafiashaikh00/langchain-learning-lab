from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
#semetic chunker per text ko divide ko sentences m break kare ga fir sabh ko apss m comapre kr k unh ka semetci diff neklay ga then kudh stdandrd deivation kare ga and mena too we just privide break point then wo threshold nekaly ga by 0.7* SD + mean =threeadshold fir jo threshold se kam same chunk tehn diff chunk ese 
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
text_splitter=SemanticChunker(
    embedding,breakpoint_threshold_type='standard_deviation',
    #we comapring two text and sd is more than 1 so on that point we split teh etxt
    #The number of chunks depends on where SemanticChunker decides to place the breakpoints, and those breakpoints depend on the chosen breakpoint strategy and its threshold.
    breakpoint_threshold_amount=1.5
    #everything relay on stadnadrd deivation
)
sample="""Ali is a farmer who grows wheat and vegetables on his land. He wakes up early every morning to water the crops and take care of his animals. Farming requires patience because the farmer depends on weather, soil quality, and water availability. The IPL is one of the most popular cricket leagues in the world. It features different teams competing in T20 cricket matches, and millions of fans watch the games every year. Players from different countries participate in the league, making it highly competitive and entertaining. A scientist studies the natural world through observation and experiments. Scientists collect data, test hypotheses, and use evidence to understand how things work.

Dr. Sarah is a scientist who studies climate change. She collects temperature data from different regions and analyzes how the Earth's climate has changed over time. Her research helps scientists understand global warming and develop better ways to protect the environment."""
docs=text_splitter.create_documents([sample])
print(docs)
print(len(docs))

""""Text ko sentences mein divide karke, sentences ke embeddings/semantic relationships ke basis par meaningful boundaries find ki jaati hain."
mean senticenses me break hugay then s1 comapre s2 if SD less trhen 1 so they are in same chunk ese compare krty kryy jis jis ka sd kam hn 1 se same chunk jha sd more than 1 to wha break wo line go to new chunk ese
Aur "1 se kam ho to same chunk" bhi fixed rule nahi hai. Threshold method decide karta hai ki semantic difference significant enough hai ya nahi.

Tumhara core idea — meaning change → breakpoint → new chunk — bilkul correct hai."""
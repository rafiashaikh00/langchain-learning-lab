#length based spiltting
#this divide the para in to chunks like we divide in 400 char ,400 tokens but disadvantage is when 400 char is over it divide in next chunk so sometimes the para have continu with next chunk so one para is divide and no give sai se menaing

"""from langchain_text_splitters import CharacterTextSplitter
#hum ek pypdf ko load krty hn dino concept ko combine krty hn

"""
text="""The History and Science of Coffee
Origins
Coffee is believed to have originated in the highlands of Ethiopia, where legend tells of a goat herder
named Kaldi who noticed his goats becoming energetic after eating certain berries. From there, coffee
cultivation and trade spread to the Arabian Peninsula, and by the 15th century it was being grown in
Yemen.
Spread Across the World
By the 17th century, coffee had made its way to Europe, sparking the creation of coffeehouses that
became centers of social and intellectual exchange. Colonial powers later introduced coffee cultivation
to the Americas and Asia, and today countries like Brazil, Vietnam, and Colombia are among the
largest producers.
The Chemistry of Caffeine
Caffeine, the active stimulant in coffee, works by blocking adenosine receptors in the brain, which
reduces feelings of tiredness. A typical cup of coffee contains between 80 and 100 milligrams of
caffeine, though this varies widely depending on the bean, roast, and brewing method.
Brewing Methods
There are many ways to brew coffee, including drip brewing, French press, espresso, pour-over, and
cold brew. Each method extracts flavors differently based on factors like water temperature, grind size,
and contact time, resulting in a wide range of tastes and strengths.
Conclusion
From a herder's curious goats to a global industry worth billions of dollars, coffee remains one of the
most widely consumed beverages in the world, deeply woven into cultures and daily routines
everywhere
""""""

#object create
spliter=CharacterTextSplitter(
    chunk_size=100,
    #"How much previous text should I repeat?"
    chunk_overlap=0,
    #separator = WHERE to split,like end of boundries, lines characters, '\n\n that mean this is para text spilttor , '\n\ to this is lien text splter , ' ' space deti hu to this si word text spilteer , '' no space k sath to char text spiltter
     separator=""

)
print("code started")
result=spliter.split_text(text)
print(result)
print("code finished")"""


# new code with pypdf loader
from langchain_text_splitters import CharacterTextSplitter
#hum ek pypdf ko load krty hn dino concept ko combine krty hn
from langchain_community.document_loaders import PyPDFLoader
#obj
loader=PyPDFLoader('rag/check/coffee.pdf')
#har page ke w.r.rt hume obj mile ga all obj come in one list
docs=loader.load()
#use kare ge etxt ko bhjy ge splitter k pas
splitter=CharacterTextSplitter(
  chunk_size=100,
  chunk_overlap=6,
  separator=""
)# ye pore docuemnt ko split kare ga mean sare ke sare docuemnt obj ko split kare dega
result=splitter.split_documents(docs)
print("code started")
print(result)
#since this is a list mean sara ek list k andr hn so we can print our first chunk
#print("this is our first chunk",result[0].page_content)
#pypdf ek doumnt ko 2 obj m dibvide kya with aoge content and meta data then kya huga spliter ek page ko jitny be chunks mm divide kare the it with document attachkrta hn us ka meta data then aghr hum text k sath use kare to meta data perserve nhu huga to meta data jitny chunks hn us k sath attach huga na k chunks jitna bra bar gen huga ye nhi huta
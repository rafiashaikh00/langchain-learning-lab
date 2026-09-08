#separtor kya kare ga phly para m divide kare ga then line by line then word me then char me aghr khai word m ivide kya wo aghr 10 se suppose kam hn to merge kare ga
#my name is natish im 35 years old i live in gurgao ab chunk size aghr 10 hn to phly wo pRA K BAS M BREAK KARE GA KYU K WO 10 SE ZEYDA HNNTO US KO LINE K BAS M KARE GA AB WO BE 10 SE ZEYDA HN TO WORDS M KARE GA AB AGHR WORD 10 SE KAM HU TO US KO MERGE KARE GA  es ki try hn us way m break kare tak k sense  bane text ka not like length
#'\n\n this for paraa , "\n this for line", " space"this for wrd,"" no space this fr char
from langchain_text_splitters import RecursiveCharacterTextSplitter
text=""" The History and Science of Coffee
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
"""

#spiltter object
spliter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0
#Aur is wale splitter mein tumhe manually separator dene ki zaroorat nahi hoti, kyunki iska default separator hierarchy already defined hota hai.
#Lekin ek important correction: ye exactly "pehle poora paragraph 10 se bada hai to line, phir word..." har level par mechanically nahi karta. Recursive splitter separators ko hierarchically try karta hai aur pieces ko chunk_size ke andar combine karta hai wherever possible.

##Tumhara main idea bilkul right hai:

#"Jitna possible ho, meaningful boundary par split karo; zarurat pade to progressively smaller boundary par jao."
)
result=spliter.split_text(text)
print(result)
print(len(result))
#mean esa hn ke wo phky para me tore g then check kare ga kya ye 300 hn aghr us se kam hn to soochy ga emrge karo ? AGHR MEREG SE ZEYDA HUGA TO WO NHI KARE GA SUPPOSE PARA WALAL BE 300 SE ZEYDA HN TO WO US KO LINE ME BREAK KARE GA THEN APPLY SMAE WAY IF MPORE THAN 300 SO AGAIN BREAK IN WORDS OR SPACE LIKE SO ONE THEN DO MERGE IF WORDS KO MILA K CHUCK SIZE =300 HU YA US  SE LESS BUT NO MORE
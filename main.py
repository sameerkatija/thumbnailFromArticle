from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
import requests
from wand.image import Image
from wand.font import Font
from wand.color import Color

#Getting Summary

url = input("Enter the url of Article: ")
article = Article(url)
article.download()
article.parse()


LANGUAGE = "english"
SENTENCES_COUNT = 10
parser = PlaintextParser.from_string(article.text, Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)
summarizer = Summarizer(stemmer)


print("Select one paragraph among the below list to use as summary")
print("===========================================================")
count = 1
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(f'{count}: {sentence}')
    count = count + 1
print("===========================================================")
paraCount = int(input('Enter the paragraph number: '))

summary = str(summarizer(parser.document, SENTENCES_COUNT)[paraCount - 1])
    

print("If you want to Select the Image from Article enter 0 or you want to use your own then press 1")
imageFlag = int(input("Enter your Choice: "))
if imageFlag < 0 or imageFlag > 1:
    raise Exception("Sorry we only accept 1 or 0 as input")

if imageFlag == 1: 
   image_url = input("Enter The Link of the Image: ")
else: 
    print("Select one image among the below list to use as Background Photo")
    print("===========================================================")
    count = 1
    imagesList = list(article.images)
    for image in imagesList:
        print(f'{count} : {image}')
        count += 1
    imageChoice = int(input("Enter the Image Number: "))
    image_url = imagesList[imageChoice - 1 ]
        
print("===========================================================")

#Print Summary on Images

image_blob = requests.get(image_url)   
with Image(blob=image_blob.content) as img:
    img.save(filename='cropped_1.jpg')
    size = img.size

widthSize = size[0]
fontSize = int(size[1] * .04)
heigthSize = int(size[1] * .30)
bottom = size[1] - int((size[1] * .40) )
captionLocY = heigthSize - int(heigthSize * .8)
# Writing on Image
with Image(width=  widthSize, height=heigthSize, background=Color('hsl(0°, 4%, 48%)')) as img:
    img.font = Font("Montserrat.otf", size=fontSize, color = 'white')
    img.caption(summary,0, captionLocY, gravity="center")
    with Image(filename='cropped_1.jpg') as canvas:
        canvas.composite(image =img, left=0, top = bottom)
        canvas.format = "jpg"
        canvas.save(filename='text_overlayed.jpg')









































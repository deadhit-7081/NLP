from textblob import TextBlob

phrase = "I reead the book"
tb_phrase = TextBlob(phrase)

#Spell Correction
correct = tb_phrase.correct()
print(correct)
phrase = TextBlob("Textblob is amazingly simple to use. What great fun!")
print(phrase.sentiment)

phrase = TextBlob("I am great")
print(phrase.sentiment.polarity)
x = phrase.sentiment.polarity
if(x<0):
    print("Neagtive")
else:
    print("posi")

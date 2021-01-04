import nltk
#nltk.download('wordnet')
#nltk.download('stopwords')
#nltk.download('punkt')
#print("Downloaded")

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

phrase = "reading the book"
# tokenize the words
words = word_tokenize(phrase)

#stemming
stemmed_words = []
for word in words:
    stemmed_words.append(stemmer.stem(word))

print(stemmed_words)

#Lemmatizing
from nltk.stem import WordNetLemmatizer

lemmetizer = WordNetLemmatizer()

lemmetized_words = []
for word in words:
    lemmetized_words.append(lemmetizer.lemmatize(word))

print(lemmetized_words)

#stopwords removal
from nltk.corpus import stopwords

stop_words = stopwords.words("english")
print(len(stop_words))

phrase = 'Here is an example sentences removing the stopwords'

words = word_tokenize(phrase)

stripped_pharse=[]
for word in words:
    if word not in stop_words:
        stripped_pharse.append(word)

print(stripped_pharse)
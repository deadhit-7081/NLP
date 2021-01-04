import spacy
from sklearn import svm
nlp = spacy.load("en_core_web_sm")

class Category:
    BOOKS="BOOKS"
    CLOTHING="CLOTHING"

train_x = ['I love the book','this is a great book','the fit is great','I love the shoes']
#giving the 4 values in train_x a lable
train_y=[Category.BOOKS,Category.BOOKS,Category.CLOTHING,Category.CLOTHING]

docs = [nlp(text) for text in train_x]
print(docs[0].vector)

train_x_wv = [x.vector for x in docs]

clf_svm_wv = svm.SVC(kernel='linear')
clf_svm_wv.fit(train_x_wv,train_y)

test_x = ["These earing hurts"]
test_docs = [nlp(text) for text in test_x]
test_x_wv = [x.vector for x in test_docs]

print(clf_svm_wv.predict(test_x_wv))

test_x = ["You look smart"]
test_docs = [nlp(text) for text in test_x]
test_x_wv = [x.vector for x in test_docs]

print(clf_svm_wv.predict(test_x_wv))
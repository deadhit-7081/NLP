from sklearn.feature_extraction.text import CountVectorizer

train_x = ['I love the book','this is a great book','the fit is great','I love the shoes']
vectorizer = CountVectorizer(binary=True) #converting train_x to vector
train_x_vectors = vectorizer.fit_transform(train_x)
print(vectorizer.get_feature_names())
print(train_x_vectors.toarray())

#building a model to classify first 2 sentences as books releted and next 2 as clothing related
class Category:
    BOOKS="BOOKS"
    CLOTHING="CLOTHING"

#giving the 4 values in train_x a lable
train_y=[Category.BOOKS,Category.BOOKS,Category.CLOTHING,Category.CLOTHING]

#simple classifier to classify the different category
from sklearn import svm

clf_svm = svm.SVC(kernel='linear') #classification model for text
clf_svm.fit(train_x_vectors,train_y)

#predict new utterences with the model
test_x = vectorizer.transform(['I like the book'])
print(clf_svm.predict(test_x))
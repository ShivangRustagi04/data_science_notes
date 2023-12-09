import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
model = MultinomialNB()

v = CountVectorizer()
df = pd.read_csv("spam.csv")
a = df.head(13)
print(a)
df['spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0)
b = df.head(34)
print(b)
X_train , X_test , y_train , y_test = train_test_split(df.Message , df.spam , test_size=0.25)
X_train_count = v.fit_transform(X_train.values) 
X_train_count.toarray()[:3]
model.fit(X_train_count,y_train)
emails = [

    'hey mohan, can we get together to watch football game tomorrow?',
    'upto 20% discount on parking, exclusive offer just for you'
]
emails_count = v.transform(X_test)
a = model.predict(emails_count)
print(a)

X_test_count = v.transform(X_test)
h = model.score(X_test_count , y_test)
print(h)
clf = Pipeline([('vectorizer', CountVectorizer()),
                ('nb',MultinomialNB())
                ])
clf.fit(X_train , y_train)
g = clf.score(X_test , y_test)
print(g)















































import pandas as pd
import os

df = pd.read_csv('movie_data.csv', encoding='utf-8')
print('列印前後各五行')
print(df.head())
print(df.tail())

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# dataframe 轉 array
#X_train = df.loc[:25000, 'review'].values
#y_train = df.loc[:25000, 'sentiment'].values
#X_test = df.loc[25000:, 'review'].values
#y_test = df.loc[25000:, 'sentiment'].values
X_train = df.loc[:25, 'review'].values
y_train = df.loc[:25, 'sentiment'].values
X_test = df.loc[49925:, 'review'].values
y_test = df.loc[49925:, 'sentiment'].values

docs = X_train[:2]
print('顯示前兩個字串')
print(docs)

print('先建立詞袋模型，再將字詞轉成特徵向量')
count = CountVectorizer()
bag = count.fit_transform(docs)

print('詞袋模型中產生', len(count.vocabulary_), '組辭彙')
print(count.vocabulary_)
print('特徵向量')
print(bag.toarray())

from sklearn.feature_extraction.text import TfidfTransformer

print('列印詞頻:')
np.set_printoptions(precision=2)
tfidf = TfidfTransformer(use_idf=True, 
                         norm='l2', 
                         smooth_idf=True)
print(tfidf.fit_transform(count.fit_transform(docs))
      .toarray())

# Logistic Learning
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV

# Stop words
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stop = stopwords.words('english')

# Token
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()

def tokenizer(text):
    return text.split()

def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]

#Learning
tfidf = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None)

param_grid = [{'vect__ngram_range': [(1, 1)],
               'vect__stop_words': [stop, None],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]},
              {'vect__ngram_range': [(1, 1)],
               'vect__stop_words': [stop, None],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'vect__use_idf':[False],
               'vect__norm':[None],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]},
              ]

lr_tfidf = Pipeline([('vect', tfidf),
                     ('clf', LogisticRegression(random_state=0))])

gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,
                           scoring='accuracy',
                           cv=5,
                           verbose=1,
                           n_jobs=-1)
# 時間很長，無法結束
gs_lr_tfidf.fit(X_train, y_train)

print('Best parameter set: %s ' % gs_lr_tfidf.best_params_)
print('CV Accuracy: %.3f' % gs_lr_tfidf.best_score_)

clf = gs_lr_tfidf.best_estimator_
print('Test Accuracy: %.3f' % clf.score(X_test, y_test))

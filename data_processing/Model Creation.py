
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import re
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from transformers import pipeline
from transformers import BertConfig, BertModel

#importing training data
trial1 = pd.read_csv('model_train_2.csv')


trial1 = trial1.dropna()


trial1 = trial1.drop(columns = ['Unnamed: 0', 'score'])


train, test = train_test_split(trial1, test_size = 0.2, random_state = 42)




#Converting sentiment to numeric values
def create_sentiment(rate):
    res = 0
    
    if rate == 'pos':
        res = 1
    elif rate == 'neg':
        res = -1
    elif rate == 'net':
        res = 0
    return res


#Applying sentiment function
trial1['senti'] = trial1['senti'].apply(create_sentiment)




#Vectorizing the data
tfidf = TfidfVectorizer(strip_accents = None,
                       lowercase = False,
                       preprocessor = None)


#Cleaning the data
def clean_data(comment):
    no_punc = re.sub(r'[^\w\s]', '', comment)
    no_digits = ''.join([i for i in no_punc if not i.isdigit()])
    return no_digits


trial1['comment'] = trial1['comment'].apply(clean_data)


X = tfidf.fit_transform(trial1['comment'])
y = trial1['senti']


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)


#Instantiating basic logisticregression model
lr = LogisticRegression(solver = 'liblinear')


lr.fit(X_train, y_train)


preds = lr.predict(X_test)


#Obtaining accuracy score
accuracy_score(preds,y_test)




X = trial1['comment']
y = trial1['senti']


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)


#Instantiating base randomforestclassifier model
rf = RandomForestClassifier()


rf.fit(X_train,y_train)


#obtaining accuracy score
preds = rf.predict(X_test)
accuracy_score(preds,y_test)




#Importing model trained through huggingface
model = pipeline(model="Bigfoottt/autotrain-f01du-emtzm", token='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')


X2 = trial1['comment']
y2 = trial1['senti']


#Creating training and test data for BertModel
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2,y2, test_size = 0.2, random_state = 42)


bert_preds = X_test2.apply(lambda x: model.predict(x))


#Obtaining only the label from the list of dictionaries
def extract_label_from_list(lst):
    if lst and isinstance(lst[0], dict):  
        return lst[0].get('label', None)  
    return None  


bert_preds = bert_preds.apply(extract_label_from_list)


#Converting the strings to ints
bert_preds = bert_preds.astype(int)


#Huggingface model has shown the best accuracy
accuracy_score(bert_preds, y_test2)



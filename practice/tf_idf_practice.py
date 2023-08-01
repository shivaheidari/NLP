import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import nltk
import string
import re
from nltk.corpus import stopwords

# Read the data
pd.set_option('display.max_colwidth', 100)
data = pd.read_csv("practice/spam.csv",encoding='latin-1')
data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
data.rename(columns={'v1':'label', 'v2':'text'}, inplace=True)
#print(data.head())

#remove punctuation 
def remove_punct(text):
    text_nonpunct = "".join([char for char in text if char not in string.punctuation])
    return text_nonpunct

#data['text_clean'] = data['text'].apply(lambda x: remove_punct(x))
#print(data.head())
#
#tokenization
def tokenize(text):
    text = re.split('\W+', text)
    return text

#data['text_tokenized'] = data['text_clean'].apply(lambda x: tokenize(x.lower()))	

#remove stopwords
def remove_stopwords(text):
    text = [word for word in text if word not in stopwords.words('english')]
    return text

#data['text_nostop'] = data['text_tokenized'].apply(lambda x: remove_stopwords(x))

print(data.head())

def clean_data(text):
    text = remove_punct(text)
    text = tokenize(text.lower())
    text = remove_stopwords(text)
    return text
data['text_clean'] = data['text'].apply(lambda x: clean_data(x))
vectorizer = TfidfVectorizer(analyzer=clean_data)
tfidf_matrix = vectorizer.fit_transform(data['text_clean'])
print(tfidf_matrix.shape)
print(vectorizer.get_feature_names())
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, recall_score, precision_score, f1_score
from sklearn.model_selection import train_test_split
import pandas as pd
from string import punctuation
import re
import nltk
stopwords = nltk.corpus.stopwords.words('english')

pd.options.display.max_colwidth = 100
data = pd.read_csv("spam.csv", encoding='latin-1')
df = pd.DataFrame(data, columns=['v1', 'v2'])
df.columns = ['label', 'text']

#cleaning the data 
def clean_text(text):
    text = "".join([word.lower() for word in text if word not in punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopwords]
    return text


df['text'] = df['text'].apply(lambda x: clean_text(x))
# tfidfvectorizer
tfidf_instance = TfidfVectorizer(analyzer=clean_text) 
tfidf = tfidf_instance.fit_transform(df['text'])

features = pd.DataFrame(tfidf.toarray())


# print(RandomForestClassifier())


x_train , x_test, y_train, y_test = train_test_split(features, df["label"], test_size=0.2, random_state=42)
print(x_train.shape, y_train.shape)

# fit a basic Randomforest model 
#view paramters and arguments of randomforestclassifier
rf_instance = RandomForestClassifier()
#print(rf_instance.get_params())


# train the model
rf_model = rf_instance.fit(x_train, y_train)
# Evaluate the model
rf_model_predict = rf_model.predict(x_test)

precision = precision_score(y_test, rf_model_predict, pos_label='spam')
recall = recall_score(y_test, rf_model_predict, pos_label='spam')
print("Precision: ", precision, "Recall: ", recall)


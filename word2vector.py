import nltk
import pandas as pd
import gensim
import numpy as np

import gensim.downloader as api
#print(api.info())

wiki_embeeding = api.load("glove-wiki-gigaword-100")

print(wiki_embeeding.most_similar("car"))


#-----------------trani our own model -----------------------------

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, recall_score, precision_score, f1_score

data = pd.read_csv("spam.csv", encoding='latin-1')
df = pd.DataFrame(data, columns=['v1', 'v2'])
df.columns = ['label', 'text']
pd.options.display.max_colwidth = 100


#cleaning the data
df["text_cleaned"] = df["text"].apply(lambda x: gensim.utils.simple_preprocess(x))

#train test split
x_train, x_test, y_train, y_test = train_test_split(df["text_cleaned"], df["label"], test_size=0.2, random_state=42)

#trian the word2vec model
model = gensim.models.Word2Vec(x_train, vector_size=100, window=5, min_count=2, workers=4)
print(model.wv.most_similar("king"))

#=----------------------------------

#w2vec = np.array(np.array([model.wv[word] for word in ls if word in model.wv.index2word])for ls in x_test)

w2v_list = [[model.wv[word] for word in ls if word in model.wv.index_to_key]for ls in x_test]

for i, v in enumerate(w2v_list):
    print(len(v))

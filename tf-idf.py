from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

vector_corpus = ["NBA is a basketball league", "Canada is a great country", "I like being in Spain. I love Seville"]
df = pd.DataFrame(vector_corpus, columns=['text'])
vectorizer = TfidfVectorizer(stop_words='english')
tfidf = vectorizer.fit_transform(df['text'])
print(tfidf.toarray())

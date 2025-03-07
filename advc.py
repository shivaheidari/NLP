import nltk
import os
from nltk.util import ngrams
import collections
#nltk.download('stopwords')
#nltk.download('wordnet')
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

base_file = open("Spark-Course-Description.txt", "r")
base_file_content = base_file.read()
base_file.close()
 
tokens = nltk.word_tokenize(base_file_content)
#print(tokens)

#remove stopwords
result = list(filter(lambda word : word not in stopwords.words('english'), tokens))
print(result)

stemresult = list(map(lambda word : PorterStemmer().stem(word), result))
print(stemresult)

lemmatizer = list(map(lambda word : WordNetLemmatizer().lemmatize(word), stemresult))
print(lemmatizer)

bigrams = ngrams(lemmatizer,2)
trigrams = ngrams(lemmatizer,3)
print(list(trigrams))

print(collections.Counter(bigrams).most_common(5))
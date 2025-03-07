import nltk
import os
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
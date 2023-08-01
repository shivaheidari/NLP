import nltk
import os
# import plaintextcorpusreader
from nltk.corpus.reader import PlaintextCorpusReader
#nltk.download('punkt')
#----------------------------------------------
corpus = PlaintextCorpusReader(os.getcwd(), "Spark-Course-Description.txt")
print(corpus.raw())
print(corpus.words())
print(corpus.sents())
print(corpus.paras())
#=---------------------------------------------
#finding the frequency distribution of words
freq_dist = nltk.FreqDist(corpus.words())
print("most common frequency:",freq_dist.most_common(10))


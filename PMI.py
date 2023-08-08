import nltk
import math 
import numpy as np
import pandas as pd
from nltk.util import ngrams

def bigram_detector(text):
    tokens = nltk.word_tokenize(text)
    bigrams_list = list(ngrams(tokens,2))
    return bigrams_list
def unigram_detector(text):
    tokens = nltk.word_tokenize(text)
    unigrams_list = list(ngrams(tokens,1))
    return unigrams_list


def pmi(word1, word2, corpus):
   #1 gram 
   onegram = unigram_detector(corpus)
   # 2 gram 
   bigram = bigram_detector(corpus)
   # tottal lenght
   total_length = len(onegram)
   # freq word1
   freq_word1 = 0
   freq_word2 = 0
   for word in corpus: 
       if word == word1:
           freq_word1 = freq_word1 + 1
       if word == word2:
            freq_word2 = freq_word2 + 1

   # freq word1 word2
        

   return 0



def count_bigrams(word1, word2, list_bigrams):
    count = 0
    for bigram in list_bigrams:
        if bigram[0] == word1 and bigram[1] == word2:
            count = count + 1
    return count


Text = "the red fox jumped over the lazy dog. the red fox lives in our neighborhood. We like the red fox. smelly cat lives in our neighborhood too. We like smelly cat."
#print(pmi("red", "fox", Text))
print(count_bigrams("red", "fox", bigram_detector(Text)))


#tokenize 
#bigram

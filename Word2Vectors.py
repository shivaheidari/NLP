from nltk import skipgrams
sent = "Insurgents killed in ongoing fighting".split()
#3 is the number of ngrams and 2 is the ngrams distance
list1=list(skipgrams(sent,3,2))
for item in list1:
    print(item)

"""
Created on Thu Nov 16 13:18:50 2017

@author: SHUBHAM
"""


import nltk

import re
import string


from nltk.corpus import stopwords


file_content = open("in.txt").read()
tokens = nltk.word_tokenize(file_content)
tokens = [token.lower() for token in tokens]


stop_words = set(stopwords.words('english'))
 
filtered_sentence = [w for w in tokens if not w in stop_words]
 
filtered_sentence = []
 
for w in tokens:
    if w not in stop_words:
        filtered_sentence.append(w)


regex = re.compile('[%s]' % re.escape(string.punctuation)) #see documentation here: http://docs.python.org/2/library/string.html

tokens_no_punctuation = []

for review in filtered_sentence:

    new_review = []
    for token in review: 
        new_token = regex.sub(u'', token)
        if not new_token == u'': 
            new_review.append(new_token)
    ''.join(new_review)
    tokens_no_punctuation.append(new_review)
    

a = []
for i in tokens_no_punctuation:
    s = "".join(i)
    a.append(s)
   
   
lemmatizer=[]

wnl = nltk.WordNetLemmatizer()
lemmatizer=[wnl.lemmatize(t) for t in a]
    
        
        
tokens_stemmer_white=[]        
tokens_stemmer_white = list(filter(None, lemmatizer))        
        
print(tokens_stemmer_white)
out = open('input.txt', 'w')
out = open('out.txt', 'w')


for item in tokens_stemmer_white:
  out.write("%s " % item)

out.close()  
with open('out.txt', 'r') as f1, open('finaloutput.txt', 'w') as f2:
    f2.write("".join([c for c in f1.read() if not c.isdigit()]))
    
f2.close()
f1.close()
#print(a)
#print ( tokens_no_punctuation)

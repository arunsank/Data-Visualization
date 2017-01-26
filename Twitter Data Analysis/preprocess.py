import pandas as pd
import pandas as pd   
import numpy as np  
import json  
import os  
from pandas.io.json import json_normalize
from nltk.corpus import stopwords  
import sys  
import re
import numpy as np
import collections,re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer




colnames= ['Text','location','status']

data=pd.DataFrame.from_csv('temp_hillary.csv')

data_ar =np.array(data)

text= data_ar[:,0]


k=list()


#print(text)


for i in range(0,11657):
    #URLless_string = re.sub(r'^https?:\/\/.*[\r\n]*', '', text[i], flags=re.MULTILINE)
    
    URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^https\s/]*))*', '', text[i],flags=re.MULTILINE)
    data_ar[i,0]=  URLless_string

  
text= data_ar[:,0] 
   
for i in range(0,11657):
    #URLless_string = re.sub(r'^https?:\/\/.*[\r\n]*', '', text[i], flags=re.MULTILINE)
    
    URLless_string1 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^https\s/]*))*', '', text[i],flags=re.MULTILINE)
    data_ar[i,0]=  URLless_string1   
     


tweets = data_ar[:,0]



filtered_words = [word for word in tweets if word not in stopwords.words('english')]


for i in range(0,len(data_ar)):
    data_ar[i,0] = filtered_words[i]


dframe= pd.DataFrame(data_ar)





dframe.to_csv('data.csv',delimiter=',')



#np.savetxt('data.csv',data_ar, delimiter=',')

count_word = re.findall(r'\w+', open('neu.csv').read().lower())

count_word1 = re.findall(r'\w+', open('pos.csv').read().lower())
count_word0 = re.findall(r'\w+', open('neg.csv').read().lower())



#console
#Counter(count_word).most_common(10)


def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])
  

l12=list()

for i in range(0,len(d2)):
    l12.append(tknzr.tokenize(d2[i]))




bigrams = [(ele, tex.split()[i+1]) for tex in text  for i,ele in enumerate(tex.split()) if i < len(tex.split())-1]

Trigrams = [(ele, tex.split()[i+1],tex.split()[i+2]) for tex in text  for i,ele in enumerate(tex.split()) if i < len(tex.split())-2]  


#console
#Counter(bigrams).most_common(10)


#console
#Counter(Trigrams).most_common(10)

    

    

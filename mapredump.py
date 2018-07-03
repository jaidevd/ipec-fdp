# coding: utf-8
import numpy as np
x = np.random.randint(1, 11, size=(100,))
x
get_ipython().magic('pinfo np.split')
np.split(x, 10)
parts = _
map(np.sum, parts)
get_ipython().magic('pinfo reduce')
mapped = map(np.sum, parts)
from functools import reduce
get_ipython().magic('pinfo reduce')
reduce(np.sum, parts)
reduce(sum, parts)
parts
reduce(sum, mapped)
mapped
list(mapped)
reduce(sum, _)
reduce(sum, map(sum, parts))
reduce(sum, map(sum, [p.tolist() for p in parts]))
parts
np.sum(parts[0])
reduce(sum, parts)
list(map(sum, parts))
reduce(sum, _)
partials = list(map(sum, parts))
partials
reduce(lambda x, y: x + y, partials)
np.sum(x)
get_ipython().magic('pinfo reduce')
from collections import Counter
c1 = Counter(a=1, b=2)
c1
c1.most_common
c1.most_common()
c1 = Counter('a b b'.split())
c2 = Counter('b c d'.split())
c1 + c2
get_ipython().magic('cd /tmp/')
get_ipython().magic('ls ')
import re
get_ipython().system('unzip sms-spam-collection-dataset.zip')
import pandas as pd
df = pd.read_csv('spam.csv')
df = pd.read_csv('spam.csv', error_bad_lines='ignore')
get_ipython().magic('pinfo pd.read_csv')
df = pd.read_csv('spam.csv', error_bad_lines=False)
get_ipython().magic('pinfo df.read_csv')
get_ipython().magic('pinfo pd.read_csv')
df = pd.read_csv('spam.csv', encoding='ascii')
df = pd.read_csv('spam.csv', encoding='latin-1')
df.head()
df.dropna(how='all', axis=0)
df.dropna(how='all', axis=1)
df.head()
df['Unnamed: 2'].unique()
df = df['v1 v2'.split()]
df.head()
df.shape
re.search(r'\w+', df.iloc[0]['v2'])
df.iloc[0]['v']
df.iloc[0]['v'2]
df.iloc[0]['v2']
re.search(r'\w+', _, re.IGNORECASE)
re.findall(r'\w+', _, re.IGNORECASE)
re.findall(r'\w+', df.iloc[0]['v2'], re.IGNORECASE)
df['v1'].value_counts()
ham = df[df['v1'] == 'ham']
spam = df[df['v2'] == 'spam']
hamwords = [re.findall(r'\w+', x.lower(), re.IGNORECASE), for x in ham['v2']]
hamwords = [re.findall(r'\w+', x.lower(), re.IGNORECASE) for x in ham['v2']]
hamwords[:5]
spam = df[df['v1'] == 'spam']
spamwords = [re.findall(r'\w+', x.lower(), re.IGNORECASE), for x in spam['v2']]
spamwords = [re.findall(r'\w+', x.lower(), re.IGNORECASE) for x in spam['v2']]
len(hamwords)
len(spamwords)
def get_sentence_wordcount(words):
    return Counter(words)
ham_sentence_wc = map(get_sentence_wordcount, hamwords)
ham_overall_wc = reduce(lambda x, y: x + y, ham_sentence_wc)
ham_overall_wc
spam_sentence_wc = map(get_sentence_wordcount, spamwords)
spam_overall_wc = reduce(lambda x, y: x + y, spam_sentence_wc)
spam_overall_wc.most_common(10)
ham_overall_wc.most_common(10)
type(spamwords)
get_ipython().magic('pinfo c1.update')
spam_naive_counter = Counter()
ham_naive_counter = Counter()
for wlist in spamwords:
    spam_naive_counter.update(wlist)
    
for wlist in hamwords:
    ham_naive_counter.update(wlist)
    
spam_overall_wc.most_common(10)
spam_naive_counter.most_common(10)
# Stopword Removal
wordlist
get_ipython().magic('whos ')
worlists = [re.findall(r'\w+', x.lower(), re.IGNORECASE) for x in df['v2'].values]
wordlists = worlists.copy()
del worlists
wordlists[:3]
len(wordlists)
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
len(ENGLISH_STOP_WORDS)
def remove_stopwords(wlist):
    nostops = []
    for w in wlist:
        if w not in ENGLISH_STOP_WORDS:
            nostops.append(w)
    return nostops
nostop_mapped = map(remove_stopwords, wordlists)
reduce(lambda x, y: x + y, [[1, 2], [2, 3]])
nostop_mapped = list(nostop_mapped)
nostop_mapped[0]
nostop_mapped[1]
len(nostop_mapped)
df_nostop = pd.DataFrame({'v1': df['v1'], 'v2': [' '.join(wlist) for wlist in nostop_mapped]})
get_ipython().magic('pinfo df_nostop')
df_nostop.head()
hamSents = df[df['v1'] == 'ham']
spamSents = df[df['v1'] == 'spam']
hamSents = hamSents['v2'].apply(lambda x: re.findall(r'\w+', x, re.IGNORECASE)).tolist()
spamSents = spamSents['v2'].apply(lambda x: re.findall(r'\w+', x, re.IGNORECASE)).tolist()
ham_wc_mapper = map(Counter, hamSents)
spam_wc_mapper = map(Counter, spamSents)
ham_wc_nostop = reduce(lambda x, y: x + y, ham_wc_mapper)
spam_wc_nostop = reduce(lambda x, y: x + y, spam_wc_mapper)
ham_wc_nostop.most_common(10)
ENGLISH_STOP_WORDS
ham_wc_mapper
ham_wc_nostop.most_common(10)
spam_wc_nostop.most_common(10)
df.head()
remove_stopwords
def remove_stopwords(wlist):
    nostops = []
    for w in wlist:
        if w.lower() not in ENGLISH_STOP_WORDS:
            nostops.append(w)
    return nostops

import pandas as pd
import numpy as np
import unicodedata
import re
import nltk
from nltk.corpus import stopwords

def basic_clean(text):
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def tokenize(text):
    tokenize = nltk.tokenize.ToktokTokenizer()
    text = tokenize.tokenize(text, return_str=True)
    return text

def stem(text):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    stemmed = ' '.join(stems)
    return stemmed

def lemmatize(text):
    wnl = nltk.stem.WordNetLemmatizer()
    lems = [wnl.lemmatize(word) for word in text.split()]
    lemmatized = ' '.join(lems)
    return lemmatized

def remove_stopwords(text, extra_words=[], exclude_words=[]):
    stopwords_ls = stopwords.words('english')
    stopwords_ls = stopwords_ls + extra_words
    [stopwords_ls.remove(word) for word in exclude_words]
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords_ls]
    stopped = ' '.join(filtered_words)
    return stopped


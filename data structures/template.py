# sentiment analysis
from textblob import TextBlob

s = TextBlob("I LOVE NLP. NLP is great! ").sentiment
print(s.polarity)
print(s.subjectivity)

# NER
import spacy

text = "Apple is looking at buying a U.K. startup for $1 billion."

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)

# POS taggging spaCy
for token in doc:
    print(token.text, token.pos_)

# Dependency parsing spaCy
for token in doc:
    print(token.text, token.dep_, token.head.text)

# feature standardization
from sklearn import preprocessing
import numpy as np

X = np.arange(100).reshape(10,10)

X_scaled = preprocessing.scale(X)
print(X_scaled.mean(axis=0))
print(X_scaled.std(axis=0))

# train/validation/test split
from sklearn.model_selection import train_test_split

y = np.arange(10)

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

X_valid, X_test, y_valid, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.5,
    random_state=42
)

# tokenization
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Hello world. I love NLP!"

word_tokens = word_tokenize(text)
sentence_tokens = sent_tokenize(text)

# stop word removal
from nltk.corpus import stopwords
stop_words = stopwords.words("english")
word_tokens_without_stop_words = [token for token in word_tokens if token.lower() not in stop_words]

# stemming
from nltk.stem import PorterStemmer
ps = PorterStemmer()
ps.stem("programming")

# lemmatization
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
wnl.lemmatize("churches")

# ngram
from nltk.util import ngrams

bigrams = ngrams(word_tokens, 2)
bigrams = [" ".join(bigram) for bigram in bigrams]

# Bag of Words using list.count()
tokens = ["python", "hello", "python"]
bow = {}

for token in set(tokens):
    bow[token] = tokens.count(token)

# Bag of Words using dict
tokens = ["python", "hello", "python"]
bow = {}

for token in tokens:
    if token not in bow:
        bow[token] = 1
    else:
        bow[token] += 1

# Bag of Words using defaultdict
from collections import defaultdict

tokens = ["python", "hello", "python"]
bow = defaultdict(int)

for token in tokens:
    bow[token] += 1

# Bag of Words using Counter
from collections import Counter

tokens = ["python", "hello", "python"]
bow = Counter(tokens)

# Bag of Words using Scikit-learn
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "python hello python",
    "hello world"
]

v = CountVectorizer()
X = v.fit_transform(corpus)

print(X.toarray())
print(v.get_feature_names_out())

# TF-IDF using Scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "the sun filled the sky",
    "the waves rolled along the shore",
    "the winter sun touched the painting",
    "the painting was a field of flowers"
]

v = TfidfVectorizer(stop_words="english")
X = v.fit_transform(corpus)

print(X.toarray())
print(v.get_feature_names_out())


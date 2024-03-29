import nltk
nltk.download('punkt')
from collections import Counter
import re


def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    tokens = nltk.word_tokenize(text)
    return tokens


tokens = get_tokens()
count = Counter(tokens)
print(count.most_common(10))
print(len(count))

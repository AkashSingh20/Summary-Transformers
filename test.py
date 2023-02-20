#only reverses,shit
# dosent work

import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
import sys


nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    word_freq = Counter()
    
    for sentence in sentences:
        words = nltk.word_tokenize(sentence.lower())
        for word in words:
            if word not in stop_words and word.isalnum():
                word_freq[ps.stem(word)] += 1
    
    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] /= max_freq
    
    sentence_scores = {}
    for sentence in sentences:
        words = nltk.word_tokenize(sentence.lower())
        score = 0
        for word in words:
            if ps.stem(word) in word_freq:
                score += word_freq[ps.stem(word)]
        sentence_scores[sentence] = score
    
    return sentence_scores

def generate_summary(text, top_n=3):
    sentence_scores = preprocess_text(text)
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:top_n]
    summary = ' '.join(top_sentences)
    return summary

with open('test.txt', 'r') as file:
    chapter_text = file.read()

summary = generate_summary(chapter_text)

print("Summary:",summary)

f = open("sum.txt", 'w')
sys.stdout = f
print (summary)
f.close()
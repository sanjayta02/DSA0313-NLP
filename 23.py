from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

text = """Machine learning is a part of artificial intelligence.
It helps computers learn from data.
Bananas are yellow in color.
Models improve with more training data."""

# Split into sentences
sentences = sent_tokenize(text)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(sentences)

# Compute coherence (similarity between adjacent sentences)
scores = []
for i in range(len(sentences) - 1):
    sim = cosine_similarity(tfidf[i], tfidf[i+1])[0][0]
    scores.append(sim)

coherence_score = sum(scores) / len(scores)

print("Sentences:\n", sentences)
print("\nCoherence Score:", round(coherence_score, 3))

if coherence_score > 0.3:
    print("Text is Coherent")
else:
    print("Text is Less Coherent")

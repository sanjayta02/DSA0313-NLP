from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documents
docs = [
    "Machine learning is a part of artificial intelligence",
    "Artificial intelligence and deep learning are related",
    "Python is used for machine learning",
    "Information retrieval uses TF IDF technique"
]

# Query
query = ["machine learning"]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(docs)

# Transform query
query_vec = vectorizer.transform(query)

# Cosine similarity
scores = cosine_similarity(query_vec, tfidf_matrix).flatten()

# Ranking
ranked_docs = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

print("Query:", query[0])
print("\nDocument Ranking:\n")

for idx, score in ranked_docs:
    print(f"Doc {idx+1}: Score={score:.3f}")
    print(docs[idx])
    print()

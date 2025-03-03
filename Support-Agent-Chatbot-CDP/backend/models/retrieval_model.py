import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_best_match(query, docs):
    corpus = list(docs.values())
    platforms = list(docs.keys())
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    query_vector = vectorizer.transform([query])
    
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    best_match_index = max(range(len(similarities)), key=lambda i: similarities[i])
    best_platform = platforms[best_match_index]
    
    relevant_text = "\n".join(docs[best_platform].split("\n")[:5])  # Return top few lines as a snippet
    return best_platform, relevant_text

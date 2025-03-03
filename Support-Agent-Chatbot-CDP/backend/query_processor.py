import json
from models.retrieval_model import retrieve_best_match

def is_irrelevant(query):
    irrelevant_keywords = ["movie", "weather", "sports", "game release"]
    return any(word in query.lower() for word in irrelevant_keywords)

def process_query(query):
    if is_irrelevant(query):
        return "I'm here to help with CDP-related queries only."
    
    docs = {}
    for platform in ["segment", "mparticle", "lytics", "zeotap"]:
        with open(f"data/{platform}_docs.json", "r") as f:
            docs.update(json.load(f))
    
    best_match_platform, relevant_text = retrieve_best_match(query, docs)
    return f"Relevant info from {best_match_platform}:\n{relevant_text}"
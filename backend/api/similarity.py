import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess(text):
    return re.sub(r'[^a-z0-9\s]', '', text.lower())

def compute_pairwise_similarity(texts):
    cleaned = [preprocess(t) for t in texts]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(cleaned)
    sim_matrix = cosine_similarity(tfidf_matrix)
    return sim_matrix.round(4).tolist()

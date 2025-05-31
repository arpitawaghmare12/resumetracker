from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

def load_resumes(folder_path):
    resumes = []
    filenames = []
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                resumes.append(f.read())
                filenames.append(file)
    return resumes, filenames

def rank_resumes(job_desc, resumes, filenames):
    docs = [job_desc] + resumes
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(docs)
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    ranked = sorted(zip(filenames, cosine_sim), key=lambda x: x[1], reverse=True)
    return ranked

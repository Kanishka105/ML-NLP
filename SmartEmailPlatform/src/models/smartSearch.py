from sklearn.feature_extraction.text import TfidfVectorizer
import os
import sys
from sklearn.metrics.pairwise import cosine_similarity
sys.path.append(os.path.abspath(".."))
from src.preprocessing.cleaning import text_cleaning_function
from src.preprocessing.nltkProcessing import nltk_stemming_function
def smartSearch(df,CombineText,query):
    vectorizer = TfidfVectorizer(
    ngram_range=(1, 3),
    min_df=2,
    max_df=0.85,
    max_features=15000,
    sublinear_tf=True)
    email_vectors = vectorizer.fit_transform(df[CombineText])
    query = text_cleaning_function(query)
    query = nltk_stemming_function(query)
    query_vector = vectorizer.transform([query])
    similarity_scores = cosine_similarity(
    query_vector,
    email_vectors)[0]
    best_index = similarity_scores.argmax()
    print("\nBest Matching Email Index :", best_index)
    print("Highest Similarity Score :", similarity_scores[best_index])
    top_k = 5
    sorted_indices = similarity_scores.argsort()[::-1]
    sorted_idx = similarity_scores.argsort()[::-1]
    for i in sorted_idx[:10]:
        print("=" * 60)
        print("Score   :", similarity_scores[i])
        print("Subject :", df.iloc[i]["subject"])
        print("Category:", df.iloc[i]["category"])
    for rank, idx in enumerate(sorted_indices[:top_k], start=1):
        print("\n" + "-" * 80)
        print(f"Rank              : {rank}")
        print(f"Similarity Score  : {similarity_scores[idx]:.4f}")
        print(f"Category          : {df.iloc[idx]['category']}")
        print(f"Subject           : {df.iloc[idx]['subject']}")
    threshold = 0.15
    filtered_indices = [
        idx
        for idx in sorted_indices
        if similarity_scores[idx] >= threshold]
    if len(filtered_indices) == 0:
        print("\nNo Matching Email Found")
    else:
        for rank, idx in enumerate(filtered_indices, start=1):
            print("\n" + "-" * 80)
            print(f"Rank              : {rank}")
            print(f"Similarity Score  : {similarity_scores[idx]:.4f}")
            print(f"Category          : {df.iloc[idx]['category']}")
            print(f"Subject           : {df.iloc[idx]['subject']}")

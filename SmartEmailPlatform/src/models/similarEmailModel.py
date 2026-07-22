from sklearn.feature_extraction.text import TfidfVectorizer
import os
import sys
from sklearn.metrics.pairwise import cosine_similarity
sys.path.append(os.path.abspath(".."))
def similarEmail(df,CombineText,email_index):
    df = df.drop_duplicates(subset=[CombineText]).reset_index(drop=True)
    subject_vectorizer = TfidfVectorizer(
    ngram_range=(1,3),
    min_df=2,
    max_df=0.85,
    max_features=5000,
    sublinear_tf=True
    )
    subject_matrix = subject_vectorizer.fit_transform(df["subject"])
    body_vectorizer = TfidfVectorizer(ngram_range=(1,3),min_df=2,max_df=0.85,max_features=15000,sublinear_tf=True)
    body_matrix = body_vectorizer.fit_transform(df["body"])
    print("="*80)
    print("SELECTED EMAIL")
    print("="*80)
    print("Category :", df.iloc[email_index]["category"])
    print("Subject  :", df.iloc[email_index]["subject"])
    print("\nBody:\n")
    print(df.iloc[email_index]["body"])
    subject_vector = subject_matrix[email_index]
    body_vector = body_matrix[email_index]
    subject_similarity = cosine_similarity(subject_vector,subject_matrix)[0]
    body_similarity = cosine_similarity(body_vector,body_matrix)[0]
    similarity_scores = (0.7 * subject_similarity +0.3 * body_similarity)
    similarity_scores[email_index] = -1
    sorted_indices = similarity_scores.argsort()[::-1]
    top_k = 5
    for rank, idx in enumerate(sorted_indices[:top_k], start=1):
        print("\n" + "-"*80)
        print(f"Rank              : {rank}")
        print(f"Similarity Score  : {similarity_scores[idx]:.4f}")
        print(f"Category          : {df.iloc[idx]['category']}")
        print(f"Subject           : {df.iloc[idx]['subject']}")
        print(f"Body Preview      : {df.iloc[idx]['body'][:200]}...")
    threshold = 0.20
    filtered_indices = [
        idx
        for idx in sorted_indices
        if similarity_scores[idx] >= threshold]
    print("\n")
    print("="*80)
    print(f"SIMILAR EMAILS ABOVE {threshold}")
    print("="*80)
    if len(filtered_indices) == 0:
        print("No Similar Email Found")
    else:
        for rank, idx in enumerate(filtered_indices, start=1):
            print("\n" + "-"*80)
            print(f"Rank              : {rank}")
            print(f"Similarity Score  : {similarity_scores[idx]:.4f}")
            print(f"Category          : {df.iloc[idx]['category']}")
            print(f"Subject           : {df.iloc[idx]['subject']}")
            print(f"Body Preview      : {df.iloc[idx]['body'][:200]}...")
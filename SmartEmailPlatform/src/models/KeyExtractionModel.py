from sklearn.feature_extraction.text import TfidfVectorizer
import os
import nltk
import sys
import pandas as pd
sys.path.append(os.path.abspath(".."))
from src.preprocessing.nltkProcessing import nltk_lemmatization_function, extract_keywords
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("averaged_perceptron_tagger")
def keyExtractModel(df,LemCombineText,email_index):
    df = df.drop_duplicates(subset=["CombineText"]).reset_index(drop=True)
    df[LemCombineText] = df[LemCombineText].apply(nltk_lemmatization_function)
    vectorizer = TfidfVectorizer(ngram_range=(1,2),min_df=2,max_df=0.85,max_features=10000,stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(df[LemCombineText])
    feature_names = vectorizer.get_feature_names_out()
    keywords = extract_keywords(email_index,10,feature_names,tfidf_matrix)
    keyword_df = pd.DataFrame( keywords,columns=["Keyword", "TF-IDF Score"])
    keyword_df.index = keyword_df.index + 1
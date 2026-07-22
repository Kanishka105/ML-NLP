import pandas as pd
from scipy.sparse import hstack
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    ConfusionMatrixDisplay
)
# check with domain and local part

def email_classification_category_model(df,body,subject,category):
    X = df[[ body,subject]]
    y = df[category]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
    body_vectorizer = TfidfVectorizer( ngram_range=(1,2),min_df=2,max_df=0.95)
    subject_vectorizer = TfidfVectorizer(ngram_range=(1,2),min_df=2,max_df=0.95)
    X_train_body = body_vectorizer.fit_transform(X_train[body])
    X_test_body = body_vectorizer.transform(X_test[body])
    X_train_subject = subject_vectorizer.fit_transform(X_train[subject])
    X_test_subject = subject_vectorizer.transform(X_test[subject])
    X_train_final = hstack([
        X_train_body,
        X_train_subject,
        ])
    X_test_final = hstack([
        X_test_body,
        X_test_subject,
        ])
    results=[]
    model = LinearSVC(random_state=42)
    model.fit(X_train_final, y_train)
    y_pred = model.predict(X_test_final)
    results.append({
            "Accuracy": accuracy_score(y_test, y_pred),
            "Precision": precision_score(y_test, y_pred, average="weighted"),
            "Recall": recall_score(y_test, y_pred, average="weighted"),
            "F1 Score": f1_score(y_test, y_pred, average="weighted"),
            "Classification_report":classification_report(y_test,y_pred),
            # "ConfusionMatrixDisplay":ConfusionMatrixDisplay(y_test,y_pred)
        })
    return results

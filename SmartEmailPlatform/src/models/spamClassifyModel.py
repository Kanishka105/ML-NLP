from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
def model_evaluation(
    text_column,
    target_column,
    df
):

    X = df[text_column]
    y = df[target_column]
    vectorizer=CountVectorizer()
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    return {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, pos_label="spam"),
        "Recall": recall_score(y_test, y_pred, pos_label="spam"),
        "F1 Score": f1_score(y_test, y_pred, pos_label="spam")
    }
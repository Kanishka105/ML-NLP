import pandas as pd

def explain_prediction(model,
                       vectorizer):

    feature_names = vectorizer.get_feature_names_out()

    coefficients = model.coef_[0]

    importance = pd.DataFrame({

        "Word":feature_names,

        "Weight":coefficients

    })

    top_positive = importance.sort_values(
        by="Weight",
        ascending=False
    ).head(10)

    top_negative = importance.sort_values(
        by="Weight"
    ).head(10)

    return top_positive, top_negative

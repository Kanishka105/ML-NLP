import pandas as pd
import re
import emoji
import string
PUNCTUATION = string.punctuation.replace("_", "")

def has_emoji(text):
    if not isinstance(text, str):
        return False
    return any(char in emoji.EMOJI_DATA for char in text)


def Trigram_fill(text):
    if pd.isna(text):
        return "NO_TRIGRAM"
    return text
def LowerCase(col):
    return col.map(lambda x: x.lower() if isinstance(x, str) else x)
def text_cleaning_function(text):
    if(text=="" ):
        return None
    text = text.lower()
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r'https?://\S+|www\.\S+', ' URL ', text)
    text = re.sub(r"\S+@\S+", " EMAIL ", text)
    text = re.sub(r"\b\d{10}\b", " PHONE ", text)
    text = emoji.demojize(text)
    # text =  re.sub(r"\s+", "", text).strip()
    text= re.sub(f"[{re.escape(PUNCTUATION)}]", "", text)
    return text
def category_validate(category,df):
    return df[df[category] != '{"mode":"full"']
def remove_email_headers(text):
    text = re.sub(r"-{2,}.*?-{2,}", " ", text)
    patterns = [
        r"From:.*",
        r"To:.*",
        r"Cc:.*",
        r"Bcc:.*",
        r"Subject:.*",
        r"Sent:.*"
    ]
    for pattern in patterns:
        text = re.sub(pattern, " ", text, flags=re.IGNORECASE)
    return text

# df=pd.read_csv("../data/raw/spamEmail/email.csv")
# df.drop_duplicates(inplace=True)
# df["Message"] = df["Message"].apply(text_cleaning_function)
# print(df["Category"].value_counts())
# can add text correction using textblob if needed, but it may be slow for large datasets
# check imbalance in the dataset and consider using techniques like SMOTE or class weighting if necessary

import pandas as pd
import re
import emoji
import string
PUNCTUATION = string.punctuation.replace("_", "")

def has_emoji(text):
    if not isinstance(text, str):
        return False
    return any(char in emoji.EMOJI_DATA for char in text)
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
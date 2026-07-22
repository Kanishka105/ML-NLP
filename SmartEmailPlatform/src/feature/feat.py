spam_keywords = {
    "free", "win", "winner", "claim", "offer",
    "prize", "cash", "urgent", "click",
    "limited", "reward", "bonus", "congratulations"
}
def count_spam_keywords(message):
    return sum(keyword in message.lower() for keyword in spam_keywords)
def count_word_count(message):
    return len(message.split())
def count_character_count(message):
    return len(message)
def feature_engineering(message):
    message = str(message)
    return {
        "Spam_Keyword_Count": count_spam_keywords(message),
        "Word_Count": count_word_count(message),
        "Character_Count": count_character_count(message)
    }

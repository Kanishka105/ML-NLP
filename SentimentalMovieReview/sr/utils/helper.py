from nltk.tokenize import sent_tokenize
def TOPIC_REPLIES():
    return {
    "acting": {
        "positive":
            "We're glad you loved the performances!",

        "negative":
            "Thank you for sharing your thoughts on the acting."
    },

    "story": {
        "positive":
            "We're happy you enjoyed the storyline!",

        "negative":
            "Thanks for your feedback about the story."
    },

    "music": {
        "positive":
            "Great to hear you enjoyed the soundtrack!",

        "negative":
            "We appreciate your opinion about the music."
    },

    "ending": {
        "positive":
            "We're delighted the ending worked for you!",

        "negative":
            "Thanks for sharing your opinion about the ending."
    }
}

def review_statistics(review, sentiment, reply):
    topic = "General"
    for key in TOPIC_REPLIES:
        if key in review.lower():
            topic = key.capitalize()
            break

    words = review.split()

    stats = {
        "Sentiment": sentiment,
        "Topic": topic,
        "Words": len(words),
        "Characters": len(review),
        "Sentences": len(sent_tokenize(review)),
        "Average Word Length": round(
            sum(len(word) for word in words) / len(words),
            2
        ),
        "Reply": reply
    }

    return stats
def check_out(review,sentiment):
    for topic in TOPIC_REPLIES:
        if topic in review:
            return TOPIC_REPLIES[topic][sentiment]

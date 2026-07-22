from nltk.tokenize import sent_tokenize
def detect_topic(review, TOPIC_REPLIES):

    review = review.lower()

    for topic in TOPIC_REPLIES:

        if topic in review:
            return topic.capitalize()

    return "General"
def review_statistics(review,
                      sentiment,
                      reply,
                      TOPIC_REPLIES):

    topic = detect_topic(review,TOPIC_REPLIES)

    words = review.split()

    if len(words):

        avg = round(
            sum(len(word) for word in words)/len(words),
            2
        )

    else:
        avg = 0

    return {

        "Sentiment":sentiment,

        "Topic":topic,

        "Words":len(words),

        "Characters":len(review),

        "Sentences":len(sent_tokenize(review)),

        "Average Word Length":avg,

        "Reply":reply
    }
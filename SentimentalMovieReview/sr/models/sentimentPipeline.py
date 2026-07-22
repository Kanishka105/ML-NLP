import sys
import os
sys.path.append(os.path.abspath(".."))
from src.models.smartReply import smart_reply
from src.models.statistics import review_statistics
from src.models.Sentimental import  predict_sentiment

def analyze_review(review, model,vectorizer,encoder,TOPIC_REPLIES):
    sentiment = predict_sentiment(review,model,vectorizer,encoder)
    reply = smart_reply(sentiment,review)
    stats = review_statistics(review,sentiment,reply,TOPIC_REPLIES)
    return stats
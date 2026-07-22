def smart_reply(sentiment, review):
    """
    Generate a smart reply for a movie review based on
    the predicted sentiment and review content.

    Parameters
    ----------
    sentiment : str
        Predicted sentiment ("positive" or "negative")

    review : str
        Original movie review

    Returns
    -------
    str
        Smart reply message
    """

    review = review.lower()

    if sentiment.lower() == "positive":

        if "acting" in review or "performance" in review:
            return (
                "🎭 Thank you for your wonderful review! "
                "We're delighted that you enjoyed the performances of the cast."
            )

        elif "story" in review or "plot" in review:
            return (
                "📖 Thank you! We're happy that you enjoyed the storyline and plot."
            )

        elif "music" in review or "soundtrack" in review:
            return (
                "🎵 Thank you! It's great to hear that you loved the movie's soundtrack."
            )

        elif "comedy" in review or "funny" in review:
            return (
                "😂 We're glad the movie made you laugh! Thank you for your positive feedback."
            )

        elif "visual" in review or "cinematography" in review:
            return (
                "🎬 Thank you! We're happy you appreciated the cinematography and visuals."
            )

        elif "ending" in review:
            return (
                "⭐ Thank you! We're delighted that the ending left a positive impression."
            )

        else:
            return (
                "😊 Thank you for your wonderful review! "
                "We're thrilled that you enjoyed the movie."
            )

    elif sentiment.lower() == "negative":

        if "boring" in review:
            return (
                "😔 We're sorry that the movie didn't keep you engaged. "
                "Thank you for sharing your honest feedback."
            )

        elif "acting" in review or "performance" in review:
            return (
                "🎭 Thank you for your feedback regarding the performances. "
                "We'll certainly take your opinion into consideration."
            )

        elif "story" in review or "plot" in review:
            return (
                "📖 We're sorry the storyline didn't meet your expectations. "
                "Thank you for your valuable feedback."
            )

        elif "music" in review or "soundtrack" in review:
            return (
                "🎵 Thank you for your comments about the soundtrack. "
                "We appreciate your honest opinion."
            )

        elif "ending" in review:
            return (
                "🎬 We appreciate your thoughts on the ending. "
                "Thank you for taking the time to share your feedback."
            )

        else:
            return (
                "😔 Thank you for your honest review. "
                "We're sorry the movie didn't meet your expectations."
            )

    else:
        return (
            "🙏 Thank you for taking the time to share your review!"
        )

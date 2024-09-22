from textblob import TextBlob

def analyze_sentiment(feedback):
    analysis = TextBlob(feedback)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

def analyze_feedback_sentiment(feedback_data):
    return [analyze_sentiment(feedback) for feedback in feedback_data]

if __name__ == "__main__":
    feedback = ["The food was great!", "The service was bad."]
    sentiments = analyze_feedback_sentiment(feedback)
    print(sentiments)

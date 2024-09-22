import matplotlib.pyplot as plt

def visualize_sentiment(sentiment_scores, output_file='sentiment_analysis.png'):
    sentiments = ['positive', 'negative', 'neutral']
    sentiment_counts = [sentiment_scores.count(sentiment) for sentiment in sentiments]

    plt.bar(sentiments, sentiment_counts)
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Feedback Sentiment Analysis')
    plt.show()

    # Save the plot to a file
    plt.savefig(output_file)
    print(f"Sentiment analysis plot saved as {output_file}")

if __name__ == "__main__":
    sentiment_scores = ['positive', 'negative', 'neutral', 'positive', 'negative']
    visualize_sentiment(sentiment_scores)

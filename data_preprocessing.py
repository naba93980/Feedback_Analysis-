import re
import json
import nltk
from nltk.corpus import stopwords


def download_stopwords():
    """
    Downloads the NLTK stopwords if they are not already present.
    """
    try:
        stop_words = set(stopwords.words('english'))
    except LookupError:
        print("Stopwords not found. Downloading...")
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))
    return stop_words


def preprocess_text(text, stop_words):
    """
    Cleans and normalizes the input text.
    """
    # Remove special characters and extra spaces
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    # Convert text to lowercase
    text = text.lower()

    # Remove stop words
    text = ' '.join([word for word in text.split() if word not in stop_words])

    return text


def load_and_preprocess_feedback(json_file):
    """
    Loads feedback data from a JSON file and preprocesses it.
    """
    # Load feedback data in the new format
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Access the 'feedback' key for each dictionary entry in the list
    feedback_data = [entry['feedback'] for entry in data]

    # Download stopwords
    stop_words = download_stopwords()

    # Preprocess each feedback entry
    return [preprocess_text(feedback, stop_words) for feedback in feedback_data]


if __name__ == "__main__":
    feedback = load_and_preprocess_feedback('feedback_data.json')
    print("Preprocessed Feedback:", feedback)

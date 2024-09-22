def filter_short_feedback(feedback_data, min_length=10):
    # Filter feedback that is too short (less than min_length words)
    return [feedback for feedback in feedback_data if len(feedback.split()) >= min_length]

if __name__ == "__main__":
    sample_feedback = ["Good", "The flight was smooth and the seats were comfortable."]
    filtered_feedback = filter_short_feedback(sample_feedback)
    print(filtered_feedback)

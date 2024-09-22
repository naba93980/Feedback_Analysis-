import os
from data_preprocessing import load_and_preprocess_feedback
from filtering import filter_short_feedback
from topic_modeling import apply_lda, display_topics
from sentiment_analysis import analyze_feedback_sentiment
# Optional:
from summarization import summarize_feedback
from visualizations import visualize_sentiment

# Step 1 and Step 2: Load and preprocess feedback

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'feedback_data.json')
print(os.path.exists(file_path))

preprocessed_feedback = load_and_preprocess_feedback(file_path)
print("Preprocessed Feedback:", preprocessed_feedback)

# Step 3: Filter short feedback
filtered_feedback = filter_short_feedback(preprocessed_feedback, min_length=5)

# Debug: Print filtered feedback to check its content
print("Filtered Feedback:", filtered_feedback)

# Step 4: Topic Modeling
lda_model, vectorizer = apply_lda(filtered_feedback)
display_topics(lda_model, vectorizer.get_feature_names_out())

# Step 5: Sentiment Analysis
sentiments = analyze_feedback_sentiment(filtered_feedback)
print(sentiments)

# Optional Steps:
# Summarization
summarized_feedback = summarize_feedback(filtered_feedback)
print(summarized_feedback)

# Visualization
visualize_sentiment(sentiments)
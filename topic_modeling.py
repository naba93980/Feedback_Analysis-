from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def apply_lda(feedback_data, n_topics=4):
    # Convert feedback to a bag of words
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    feedback_matrix = vectorizer.fit_transform(feedback_data)

    # Apply Latent Dirichlet Allocation (LDA)
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(feedback_matrix)

    return lda, vectorizer

def display_topics(model, feature_names, no_top_words=10):
    for topic_idx, topic in enumerate(model.components_):
        print(f"Topic {topic_idx}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))

if __name__ == "__main__":
    feedback = ["the food was good", "the service was slow"]
    lda_model, vectorizer = apply_lda(feedback)
    display_topics(lda_model, vectorizer.get_feature_names_out())

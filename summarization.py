from transformers import pipeline

def summarize_feedback(feedback_data):
    summarizer = pipeline("summarization", device=0)
    summarized_feedback = []
    for feedback in feedback_data:
        summary = summarizer(feedback, max_length=4, min_length=2, do_sample=False)
        summarized_feedback.append(summary[0]['summary_text'])
    return summarized_feedback

if __name__ == "__main__":
    feedback = ["The food was ok, but the AC was too cold."]
    summarized = summarize_feedback(feedback)
    print(summarized)

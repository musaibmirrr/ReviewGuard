from textblob import TextBlob

# Sample text data for analysis
sample_texts = [
    "I love this product! It's amazing.",  # Expected: Positive
    "This is the worst experience I've ever had.",  # Expected: Negative
    "It's okay, not great but not bad either.",  # Expected: Neutral
    "Absolutely fantastic service!",  # Expected: Positive
    "Not what I expected, pretty disappointed."  # Expected: Negative
]

# Define expected labels based on common sentiment knowledge
expected_labels = ['Positive', 'Negative', 'Neutral', 'Positive', 'Negative']

# Analyze sentiment using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Returns a float polarity score

# Classify sentiment based on polarity
def classify_sentiment(polarity):
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# Analyze and classify sentiments
predicted_labels = []
for text in sample_texts:
    polarity = analyze_sentiment(text)
    sentiment = classify_sentiment(polarity)
    predicted_labels.append(sentiment)

# Calculate accuracy
correct_predictions = sum(pred == expected for pred, expected in zip(predicted_labels, expected_labels))
accuracy = (correct_predictions / len(expected_labels)) * 100

# Output the results
print(f'Predicted Labels: {predicted_labels}')
print(f'Expected Labels: {expected_labels}')
print(f'Accuracy: {accuracy:.2f}%')

import nltk

from nltk.tokenize import word_tokenize
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy

nltk.download('punkt')

data = [
    ("Free money!!!", "spam"),
    ("Hi, how are you?", "ham"),
    ("Win a free iPhone now", "spam"),
    ("Are we still meeting tomorrow?", "ham"),
    ("Limited offer! Call now!", "spam"),
    ("Don't forget our lunch meeting", "ham"),
]

# Create feature extractor
def extract_features(text):
    words = word_tokenize(text.lower())
    return {word: True for word in words}

# Apply feature extractor
feature_set = [(extract_features(text), label) for (text, label) in data]

# Split into train and test
train_set = feature_set[:4]
test_set = feature_set[4:]

# Train classifier
classifier = NaiveBayesClassifier.train(train_set)

print("Accuracy:", accuracy(classifier, test_set))
classifier.show_most_informative_features()


msg = "Congratulations! You have won a free ticket"
features = extract_features(msg)
print("Prediction:", classifier.classify(features))
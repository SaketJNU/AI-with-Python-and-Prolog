import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download()
nltk.download('punkt')
nltk.download('stopwords')

# Sample paragraph
paragraph = "This is a sample paragraph. It contains punctuation, and stop words like 'is', 'a', and 'the'."

# Tokenize the paragraph into words
words = word_tokenize(paragraph)

# Convert to lowercase
words = [word.lower() for word in words]

# Remove punctuation
words = [word for word in words if word not in string.punctuation]
print("List containing all words\n", words)
# Remove stop words
stop_words = set(stopwords.words('english'))
print("Set of Stop Word\n", stop_words)
filtered_words = [word for word in words if word not in stop_words]

# Output result
print("Set of filtered words\n",filtered_words)
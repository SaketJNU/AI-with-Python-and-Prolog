import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
nltk.download()  # This is added to fix a bug
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')  # For lemmatizer
nltk.download('averaged_perceptron_tagger')  # Optional: for better lemmatization

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Function to map NLTK POS tags to WordNet tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun

# Get user input
text = input("Enter a sentence: ")

# Tokenize
tokens = word_tokenize(text)
print("List of tokens:\n", tokens)

# POS tagging
pos_tags = nltk.pos_tag(tokens)
print("List of POS Tags:\n", pos_tags)

# Perform stemming and lemmatization
print("\nWord\tStem\tLemma")
print("-" * 30)
for word, tag in pos_tags:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word, get_wordnet_pos(tag))
    print(f"{word}\t{stem}\t{lemma}")
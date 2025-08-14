import nltk
from nltk.tokenize import word_tokenize

# Download necessary resources (only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence
tokens = word_tokenize(sentence)
print("List of tokens: \n", tokens)

# Perform POS tagging
pos_tags = nltk.pos_tag(tokens)
print("List of pos tags: \n", pos_tags)

# Output
print("\nPOS Tags:")
for word, tag in pos_tags:
    print(f"{word} --> {tag}")
# Word Sense Disambiguation using Lesk Algorithm

import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Download required resources (Run only once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Input sentence and ambiguous word
sentence = "I went to the bank to deposit money"
ambiguous_word = "bank"

# Tokenize sentence
tokens = word_tokenize(sentence)

# Apply Lesk Algorithm
sense = lesk(tokens, ambiguous_word)

# Output result
print("Sentence:", sentence)
print("Ambiguous Word:", ambiguous_word)

if sense:
    print("\nCorrect Sense Found:")
    print("Synset:", sense.name())
    print("Definition:", sense.definition())
    print("Example:", sense.examples())
else:
    print("No sense found.")

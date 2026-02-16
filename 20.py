import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# Download (run once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

sentence = "I went to the bank to deposit money"
word = "bank"

tokens = word_tokenize(sentence)
sense = lesk(tokens, word)

print("Sentence:", sentence)
print("Word:", word)

if sense:
    print("Sense:", sense.name())
    print("Meaning:", sense.definition())
else:
    print("No sense found")

import nltk

# Download required resources (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input text
text = "NLP is an interesting subject"

# Tokenization
words = nltk.word_tokenize(text)

# POS tagging
pos_tags = nltk.pos_tag(words)

# Output
print("Word \t POS Tag")
for word, tag in pos_tags:
    print(word, "\t", tag)

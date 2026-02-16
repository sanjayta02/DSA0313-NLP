# Simple probabilistic POS tagger

# Training data: word -> {tag: probability}
prob_model = {
    "I": {"PRP": 1.0},
    "love": {"VB": 0.7, "NN": 0.3},
    "NLP": {"NNP": 1.0},
    "is": {"VBZ": 1.0},
    "fun": {"JJ": 0.6, "NN": 0.4}
}

# Input sentence
sentence = "I love NLP"

# Tokenization
words = sentence.split()

# POS tagging using highest probability
print("Word \t POS Tag")
for word in words:
    if word in prob_model:
        tag = max(prob_model[word], key=prob_model[word].get)
    else:
        tag = "NN"   # Default tag
    print(word, "\t", tag)

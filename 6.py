import random

# Sample training text
text = "nlp is fun and nlp is interesting and nlp is useful"

# Tokenization
words = text.split()

# Create bigram dictionary
bigrams = {}

for i in range(len(words) - 1):
    key = words[i]
    next_word = words[i + 1]
    
    if key not in bigrams:
        bigrams[key] = []
    bigrams[key].append(next_word)

# Text generation
current_word = random.choice(words)
generated_text = [current_word]

for _ in range(10):
    if current_word in bigrams:
        current_word = random.choice(bigrams[current_word])
        generated_text.append(current_word)
    else:
        break

# Output
print("Generated Text:")
print(" ".join(generated_text))

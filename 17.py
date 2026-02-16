# Accessing WordNet using NLTK

# Step 1: Import NLTK and WordNet
import nltk
from nltk.corpus import wordnet as wn

# Step 2: Download WordNet (Run only once)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Step 3: Input word
word = "bank"

# Step 4: Get synsets of the word
synsets = wn.synsets(word)

print(f"Synsets for the word '{word}':\n")

# Step 5: Display meanings, synonyms, and examples
for i, syn in enumerate(synsets, 1):
    print(f"Synset {i}: {syn.name()}")
    print("Definition:", syn.definition())
    
    # Synonyms
    synonyms = [lemma.name() for lemma in syn.lemmas()]
    print("Synonyms:", synonyms)
    
    # Example sentences
    examples = syn.examples()
    if examples:
        print("Example:", examples[0])
    
    print("-" * 50)

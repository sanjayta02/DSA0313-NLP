import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define PCFG Grammar
grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | 'John' [0.4]
VP -> V NP [1.0]
Det -> 'the' [1.0]
N -> 'dog' [0.5] | 'cat' [0.5]
V -> 'sees' [1.0]
""")

# Create Parser
parser = ViterbiParser(grammar)

# Input sentence
sentence = "John sees the dog".split()

# Parse sentence
for tree in parser.parse(sentence):
    print("Most Probable Parse Tree:")
    print(tree)

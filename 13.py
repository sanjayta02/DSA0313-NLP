import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

# Define Grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

# Create Parser
parser = RecursiveDescentParser(grammar)

# Input sentence
sentence = "the cat chased the dog".split()

# Generate Parse Tree
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()

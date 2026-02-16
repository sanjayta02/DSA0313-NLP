import nltk
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag, RegexpParser

# Download (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

sentence = "The intelligent student reads a complex book in the library"

# Tokenize & POS tag
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define NP grammar
grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
chunk_parser = RegexpParser(grammar)
tree = chunk_parser.parse(tagged)

print("Noun Phrases and Meanings:\n")

for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
    np = " ".join(word for word, tag in subtree.leaves())
    print("Noun Phrase:", np)

    # Get meaning of main noun (last word)
    main_noun = subtree.leaves()[-1][0]
    synsets = wordnet.synsets(main_noun)

    if synsets:
        print("Meaning:", synsets[0].definition())
    else:
        print("Meaning: Not found")

    print()

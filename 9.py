import re

# Rule-based POS tagging function
def rule_based_pos_tagger(sentence):
    words = sentence.split()

    print("Word\tPOS Tag")

    for word in words:
        if re.fullmatch(r'\d+', word):
            tag = "CD"       # Cardinal Number
        elif re.fullmatch(r'(a|an|the)', word.lower()):
            tag = "DT"       # Determiner
        elif re.fullmatch(r'.*ing$', word.lower()):
            tag = "VBG"      # Verb Gerund
        elif re.fullmatch(r'.*ed$', word.lower()):
            tag = "VBD"      # Verb Past
        elif re.fullmatch(r'.*ly$', word.lower()):
            tag = "RB"       # Adverb
        elif re.fullmatch(r'.*ous$|.*ful$|.*able$|.*ive$', word.lower()):
            tag = "JJ"       # Adjective
        elif re.fullmatch(r'.*s$', word.lower()):
            tag = "NNS"      # Plural Noun
        elif word[0].isupper():
            tag = "NNP"      # Proper Noun
        else:
            tag = "NN"       # Default Noun

        print(f"{word}\t{tag}")


# Input sentence
sentence = "The boys are playing happily in the Garden"

# Run tagger
rule_based_pos_tagger(sentence)

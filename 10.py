# Transformation Based Tagging (Simple Version)

def initial_tag(word):
    if word.endswith("ing"):
        return "VBG"   # Verb Gerund
    elif word.endswith("ed"):
        return "VBD"   # Past Verb
    elif word.endswith("ly"):
        return "RB"    # Adverb
    elif word[0].isupper():
        return "NNP"   # Proper Noun
    else:
        return "NN"    # Default Noun


def transform_tags(words, tags):
    new_tags = tags.copy()

    for i in range(len(words)):
        # Rule 1: If previous word is "to" and tag is NN → VB
        if i > 0 and words[i-1].lower() == "to" and new_tags[i] == "NN":
            new_tags[i] = "VB"

        # Rule 2: If word ends with 's' and tag is NN → NNS (plural noun)
        if words[i].endswith("s") and new_tags[i] == "NN":
            new_tags[i] = "NNS"

    return new_tags


# Input sentence
sentence = "Ram likes to play games quickly"
words = sentence.split()

# Step 1: Initial tagging
initial_tags = [initial_tag(word) for word in words]

# Step 2: Apply transformation rules
final_tags = transform_tags(words, initial_tags)

# Output
print("Words:        ", words)
print("Initial Tags: ", initial_tags)
print("Final Tags:   ", final_tags)

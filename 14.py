# Simple Agreement Checker using CFG rules

# Grammar with agreement
grammar = {
    "S": [("NP_sg", "VP_sg"), ("NP_pl", "VP_pl")],
    "NP_sg": ["he", "she", "ram"],
    "NP_pl": ["they", "we", "students"],
    "VP_sg": ["runs", "eats", "plays"],
    "VP_pl": ["run", "eat", "play"]
}

def check_agreement(sentence):
    words = sentence.lower().split()
    if len(words) != 2:
        return False

    subject, verb = words

    # Check singular agreement
    if subject in grammar["NP_sg"] and verb in grammar["VP_sg"]:
        return True

    # Check plural agreement
    if subject in grammar["NP_pl"] and verb in grammar["VP_pl"]:
        return True

    return False


# Input sentence
sentence = "he runs"

# Check agreement
if check_agreement(sentence):
    print("Agreement Correct")
else:
    print("Agreement Incorrect")

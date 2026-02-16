# Simple Dialog Act Recognition

def classify_dialog(sentence):
    s = sentence.lower()

    if s.endswith("?"):
        return "Question"
    elif any(word in s for word in ["hello", "hi", "good morning", "hey"]):
        return "Greeting"
    elif any(word in s for word in ["please", "could you", "can you"]):
        return "Request"
    else:
        return "Statement"


dialog = [
    "Hello, how are you?",
    "I am fine.",
    "Can you help me with this problem?",
    "This is a simple example."
]

for line in dialog:
    print("Sentence:", line)
    print("Dialog Act:", classify_dialog(line))
    print()

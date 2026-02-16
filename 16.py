# Named Entity Recognition using SpaCy

# Step 1: Import spacy
import spacy

# Step 2: Load English model
nlp = spacy.load("en_core_web_sm")

# Step 3: Input text
text = "Apple was founded by Steve Jobs in California on April 1, 1976."

# Step 4: Process the text
doc = nlp(text)

# Step 5: Print Named Entities
print("Named Entities in the text:\n")

for ent in doc.ents:
    print(f"Entity: {ent.text}  |  Label: {ent.label_}")

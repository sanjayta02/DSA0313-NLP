from transformers import pipeline

# Load translation pipeline (English → French)
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")

# Input text
text = "Machine learning is a part of artificial intelligence."

# Translate
result = translator(text)

# Output
print("English:", text)
print("French:", result[0]['translation_text'])

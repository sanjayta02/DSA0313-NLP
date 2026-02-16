import re

text = "My phone number is 9876543210 and my ID is 123."

# Match all numbers
numbers = re.findall(r'\d+', text)
print("Numbers found:", numbers)

# Search for a specific word
word = re.search(r'phone', text)
if word:
    print("Word 'phone' found")
else:
    print("Word not found")
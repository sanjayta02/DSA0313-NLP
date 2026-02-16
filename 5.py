from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "played", "happiness", "studies"]

for word in words:
    print(word, "->", stemmer.stem(word))
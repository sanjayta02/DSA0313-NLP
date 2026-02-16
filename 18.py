# Simple FOPC Parser in Python
import re

# Define logical operators
operators = {"AND", "OR", "NOT", "IMPLIES"}

# Function to check variable (lowercase)
def is_variable(token):
    return token.islower() and token.isalpha()

# Function to check constant (uppercase single letter or word)
def is_constant(token):
    return token[0].isupper()

# Function to parse expression
def parse_fopc(expression):
    print("Input Expression:", expression)
    print("\nParsed Components:\n")

    # Tokenize using regex
    tokens = re.findall(r"[A-Za-z_]+|\(|\)|,", expression)

    for token in tokens:
        if token in operators:
            print(f"{token}  --> Logical Operator")

        elif "(" in token or ")" in token or token == ",":
            continue

        elif token[0].isupper() and "(" in expression:
            print(f"{token}  --> Predicate")

        elif is_variable(token):
            print(f"{token}  --> Variable")

        elif is_constant(token):
            print(f"{token}  --> Constant")


# Example FOPC expression
expr = "Loves(John, x) AND Knows(x, Mary)"

# Run parser
parse_fopc(expr)

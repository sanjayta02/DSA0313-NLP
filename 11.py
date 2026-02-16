# Simple Top-Down Parser (Recursive Descent)

# Grammar:
# S -> aSb | ab

def parse_S(string, i):
    # Rule S -> ab
    if i + 1 < len(string) and string[i] == 'a' and string[i+1] == 'b':
        return i + 2

    # Rule S -> aSb
    if i < len(string) and string[i] == 'a':
        j = parse_S(string, i + 1)
        if j != -1 and j < len(string) and string[j] == 'b':
            return j + 1

    return -1


# Input string
input_string = "aaabbb"

# Start parsing
result = parse_S(input_string, 0)

# Check acceptance
if result == len(input_string):
    print("String Accepted")
else:
    print("String Rejected")

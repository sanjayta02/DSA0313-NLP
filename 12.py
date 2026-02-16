# Simple Earley Parser

def earley_parser(words, grammar, start_symbol):
    n = len(words)
    chart = [set() for _ in range(n + 1)]

    # State format: (LHS, RHS, dot_position, start_index)
    chart[0].add((start_symbol, tuple(grammar[start_symbol][0]), 0, 0))

    for i in range(n + 1):
        changed = True
        while changed:
            changed = False
            for state in list(chart[i]):
                lhs, rhs, dot, start = state

                # If not complete
                if dot < len(rhs):
                    next_symbol = rhs[dot]

                    # Predictor
                    if next_symbol in grammar:
                        for prod in grammar[next_symbol]:
                            new_state = (next_symbol, tuple(prod), 0, i)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

                    # Scanner
                    elif i < n and next_symbol == words[i]:
                        chart[i + 1].add((lhs, rhs, dot + 1, start))

                # Completer
                else:
                    for prev in list(chart[start]):
                        plhs, prhs, pdot, pstart = prev
                        if pdot < len(prhs) and prhs[pdot] == lhs:
                            new_state = (plhs, prhs, pdot + 1, pstart)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

    # Check acceptance
    for state in chart[n]:
        lhs, rhs, dot, start = state
        if lhs == start_symbol and dot == len(rhs) and start == 0:
            return True
    return False


# Example Grammar
# S -> a S b | a b
grammar = {
    'S': [['a', 'S', 'b'], ['a', 'b']]
}

# Input string
sentence = "aaabbb"
words = list(sentence)

# Run parser
if earley_parser(words, grammar, 'S'):
    print("String Accepted")
else:
    print("String Rejected")

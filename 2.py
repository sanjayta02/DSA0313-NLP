def ends_with_ab(string):
    state = 0

    for char in string:
        if state == 0:
            if char == 'a':
                state = 1
        elif state == 1:
            if char == 'b':
                state = 2
            else:
                state = 0

    return state == 2

# Test strings
strings = ["cab", "abab", "ab", "abc", "aab"]

for s in strings:
    print(s, "->", ends_with_ab(s))

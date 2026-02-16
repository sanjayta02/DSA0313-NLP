def pluralize(noun):
    if noun.endswith('y'):
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + 'es'
    else:
        return noun + 's'

nouns = ["cat", "bus", "baby", "box"]

for n in nouns:
    print(n, "->", pluralize(n))

alphabet = dict({'a': '\U0001f170', 'b':'\U0001f171', 'c':'\u00A9', 'd': '\U0001f31b', 'e': '\U0001F4e8'})

def translate(word):
    result = ""
    for w in word:
        if w in alphabet:
            result += alphabet[w]
        else:
            result += w
    return result
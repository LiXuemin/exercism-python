letterSet = [chr(i) for i in range(65,91)]
print(" ".upper())

def is_pangram(sentence):
    for i in sentence:
        if i.upper() in letterSet:
            letterSet.remove(i.upper())
    if len(letterSet) != 0:
        return False
    return True
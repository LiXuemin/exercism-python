import re
def word_count(phrase):
    word_dict = {}
    words = phrase.split()
    t = ".:"
    for word in words:

        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def word_count1(phrase):
    return re.split(r'[;,]', phrase)

print(word_count1("First: don't laugh. Then: don't cry."))
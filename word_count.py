import re
def word_count(phrase):
    word_dict = {}
    words = re.split('_|:|\s|(?<!\d)[,.](?!\d)', phrase.lower())
    for word in words:
        if not word.isspace() and len(word) > 0:
            word = word.strip('\'!&@$%^&')
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict


# def word_count1(phrase):
#     return re.split(':|\s|(?<!\d)[,.](?!\d)', phrase)
#
# print(word_count1("First: don't laugh. Then: don't cry."))
# print(word_count1("Joe can't tell between 'large' and large."))
# print(word_count1('rah rah ah ah ah\nroma roma ma\n'
#                        'ga ga oh la la\nwant your bad romance'))
print("'sss  ".strip("'"))
def is_isogram(string):
    a = list(string)
    n = len(a)
    for i in range(n):
        if a[i].isalpha() and string.count(a[i]) != 1:
            return False
    return True

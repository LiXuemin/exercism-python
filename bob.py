def hey(phrase):
    if phrase.isupper():
        return "Whoa, chill out!"
    if len(phrase.strip())>0 and phrase.strip()[-1] == "?":
        return "Sure."
    if len(phrase.strip("\t\n\r ")) == 0:
        return "Fine. Be that way!"
    else:
        return "Whatever."
def consonant_or_vowel(char):
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        return "%c is vowel" % char
    else:
        return "%c is consonant" % char


character = input("enter your char : ")

print(consonant_or_vowel(character))

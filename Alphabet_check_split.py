"""Comparing first alphabet of two different words,
if alphabet is similar than  the output will be TRUE or else FALSE """

words = str(input("any two words: "))

def split(words):
    if words.upper().split()[0][0] == words.upper().split()[1][0]: # Ss = words.upper().split()[0][0] == words.upper().split()[1][0]
                                                                    #return SS ==> no need to write if or else statement it will directly give true/false
        print(True)
    else:
        print(False)

split(words)
# As a user enters two words of his choice, the spacing part is comparing words as to diff values of list.


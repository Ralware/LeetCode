def lengthOfLastWord(Sentence):
    Sentence = Sentence.strip()[::-1]
    Word = ""
    for Val in Sentence:

        if Val != " ":
            Word += Val
        else:
            return len(Word)
        

    return len(Word)

print(lengthOfLastWord("a"))
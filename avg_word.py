#in this exercise I will calculate the average length of a word in a given sentence

def avg_len(sentence):
    list_of_punc = ['!','?',':','.', ',']
    for punc in list_of_punc:
        sentence = sentence.replace(punc, '')
    words = sentence.split()
    return round(sum([len(word) for word in words])/len(words))

print(avg_len('I love boobiezer the booban'))
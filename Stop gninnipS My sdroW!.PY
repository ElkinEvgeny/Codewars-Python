def spin_words(sentence):
    slovar=[]
    for i in sentence.split():
        if len(i)>=5:
            slovar.append(i[::-1])
        else: slovar.append(i)
    return ' '.join (slovar)
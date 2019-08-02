def seimano(array):
    eluwa = ''
    for i in range(len(array)):

        if(array[i] == array[-1]):

            eluwa = eluwa + 'i ' + array[i]
        else:

            eluwa = eluwa + array[i] + ','

    return eluwa




spam = ['Jabłka', 'Banany', 'Tofu', 'Koty']
witam = seimano(spam)
print(witam)

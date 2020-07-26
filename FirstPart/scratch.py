def fun(array):
    str = ''
    for i in range(len(array)):

        if(array[i] == array[-1]):

            str = str + 'i ' + array[i]
        else:

            str = str + array[i] + ','

    return str




spam = ['Jabłka', 'Banany', 'Tofu', 'Koty']
result = fun(spam)
print(witam)

def collatz(number):

    try:
        int(number)
    except ValueError:
        print('Podana zostala na pewno nie liczba')


    if number % 2 == 0:

        number = number // 2
        print(number)
        return number
    else:
        number = (number * 3) + 1
        print(number)
        return number


number = int(input('Enter ur value: '))
while liczba != 1:
    liczba = collatz(liczba)


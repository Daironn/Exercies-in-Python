import os
def MadLips(slowo = "PRZYMIOTNIK", slowo2 = "RZECZOWNIK", slowo3 = "CZASOWNIK", slowo4 = "RZECZOWNIK"):
    slowa = ["Wczoraj",slowo,"panda","weszła","na",slowo2,"i","zaczęła",slowo3,"Pobliska",slowo4,"nie","ucierpiała","na","skutek","tych","zdarzeń"]

    os.chdir("C:\\Users\Daorin\Documents\Śmieci")
    file = open('testfile.txt', 'w')

    for i in range(0, len(slowa)):
        file.write(slowa[i]+" ")
        if i == 8:
            file.write(slowa[i] + ". ")
        if i == len(slowa)-1:
            file.write(slowa[i] + ".")

    return slowa
    file.close()

first_input = input("Zaczynamy?: Y/N")
while first_input == "Y" or first_input == "y":
    second_input = input("PRZYMIOTNIK: ")
    third_input = input("RZECZOWNIK: ")
    fourth_input = input("CZASWONIK: ")
    fifth_input = input("RZECZOWNIK: ")
    print(MadLips(second_input,third_input,fourth_input,fifth_input))
    first_input = input("Kontynuujemy?: Y/N")
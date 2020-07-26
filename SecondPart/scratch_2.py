def mystrip(string, char = " "):
    liczba = 0
    liczba2 = len(string)-1

    strumien = ""
    while True:
        if(string[liczba] == char):
            liczba+=1
        else:
            break

    while True:
        if(string[liczba2] == char):
            liczba2-=1
        else:
            break
    for i in range(liczba, liczba2+1):
        strumien+=string[i]

    return strumien

print(mystrip(  "  --**test**********----", "-"  ))
import re
def passchecker(password):
    if len(password) < 8:
        return "TOO SHORT"
    elif re.search(r"\d", password) == None:
        return "Nie ma cyfry"
    elif re.search(r"[a-z]", password) == None:
        return "Nie ma małej litery"
    elif re.search(r"[A-Z]", password) == None:
        return "Nie ma dużej litery"
    elif re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) == None:
        return "Nie ma znaku specjalnego"
    else:
        return "STRONG"


print (passchecker("Doria!no1skar"))
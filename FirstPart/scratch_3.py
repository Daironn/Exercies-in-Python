def displayInventory(inv):

    print("Inwentarz")
    item_total = 0
    for k, v in inv.items():

        print(k +":", v)
        item_total+=1
    print("Całkowita liczba przedmiotów: "+ str(item_total))

def addToInventory(inv, loot):

    for i in loot:
     if i in inv.keys():
         inv[i] +=1
    else:
         inv.setdefault(i , 1)

postac = {
    'lina' : 1,
    'pochodnia' : 8,
    'złote monety' : 5,
    'sztylet' : 1,
    'strzała' : 66
}

sweetloor = [
    'złote monety',
    'sztylet',
    'złote monety',
    "dragon's bone"
]
displayInventory(postac)
addToInventory(postac, sweetloor)
displayInventory(postac)
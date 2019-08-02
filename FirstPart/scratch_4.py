def printtable(table):
    pierwszy = int(len(table[0][0]) + len(table[1][0]) + len(table[2][0]))
    drugi = int(len(table[0][1]) + len(table[1][1]) + len(table[2][1]))
    trzeci = int(len(table[0][2]) + len(table[1][2]) + len(table[2][2]))
    czwarty = int(len(table[0][3]) + len(table[1][3]) + len(table[2][3]))

    lista = [pierwszy, drugi, trzeci, czwarty]
    siema = max(lista)
    for i in range(4):
        print()
        for j in range(3):

            print(str(table[j][i].rjust(siema)), end = "")



tableData = [['jabłka', 'pomararancze', 'wiśnie', 'banany'],
             ['Alicja','Bob','Karol','Dawid'],
             ['psy','koty','łosie','gęsi']]

printtable(tableData)


import os, shutil, re

danuta = re.compile(r'''(/w)*.bsp''')
danutaa = re.compile(r'''(/w)*.nav''')
def search_and_copy(Path):

    for folderPath, folderName, filenames in os.walk(Path):

        for filename in filenames:

            if danuta.search(filename) != None or danutaa.search(filename) != None:

                shutil.copy(os.path.join(folderPath, filename),'E:\\Mapki surf' )






search_and_copy('D:\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\maps')
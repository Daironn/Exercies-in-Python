import glob
import re

phonenumber = re.compile(r'\d\d\d \d\d\d \d\d\d')
path = 'C:\\Users\Daorin\Documents\Śmieci\*.txt'
files = glob.glob(path)

for name in files:
    with open(name) as f:
        contents =  f.read()
        search = phonenumber.search(contents)
        print(search)
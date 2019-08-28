import os

def search_and_remove(FilePath):

    for dirPath, dirNames, filenames in os.walk(FilePath):

        for filename in filenames:

            if os.path.getsize(os.path.join(dirPath, filename)) >= 0:

                os.remove(os.path.join(dirPath, filename))

search_and_remove('C:\\Users\Daorin\Pictures\elo')
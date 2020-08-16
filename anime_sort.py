import os
import shutil

from time import sleep
from distutils.dir_util import copy_tree

def clean_directory_name (id):
    clean_name = list (id)

    while ('[' in clean_name):
        start = clean_name.index('[')
        end = clean_name.index(']') + 1

        for i in range (end - start):
            del (clean_name[start])
    
    if clean_name[0] == " ":
        del (clean_name[0])

    while clean_name[len(clean_name) - 1] == " ":
        del (clean_name[len(clean_name) - 1])

    clean_name = "".join(clean_name)
    return clean_name

def clean_episode_name (id):
    clean_name = list (id)

    while ('[' in clean_name):
        start = clean_name.index('[')
        end = clean_name.index(']') + 1

        for i in range (end - start):
            del (clean_name[start])
    
    if clean_name[0] == " ":
        del (clean_name[0])

    while clean_name[len(clean_name) - EXTENSION_OFFSET] == " ":
        del (clean_name[len(clean_name) - EXTENSION_OFFSET])

    clean_name = "".join(clean_name)
    return clean_name

download_path = 'C:\\Users\\Xavier\\Desktop\\download' 
series_path = 'C:\\Users\\Xavier\\Documents\\series\\' 
path_separator = '\\'  

EXTENSION_OFFSET = 5

os.chdir(download_path)

cwd = os.getcwd()

names = os.listdir(cwd)
new_name = []
episode_name = []
folder_name = []
file_size = 0

for name in names:
    if os.path.isdir (name):
        copy_path = download_path + path_separator + name 
        paste_path = series_path + clean_directory_name (name)

        if not os.path.exists(paste_path):
            os.mkdir (paste_path)
        
        copy_tree (copy_path, paste_path)
        sleep (2)

        os.chdir (paste_path)

        files =  os.listdir (paste_path)

        for f in files:
            new_file_name = clean_episode_name (f)
            os.rename (f, new_file_name)

        shutil.rmtree(copy_path)

        continue

    new_name = list (name)
    
    while ('[' in new_name):
        start = new_name.index('[')
        end = new_name.index(']') + 1

        for i in range (end - start):
            del (new_name[start])
    
    if new_name[0] == " ":
        del (new_name[0])

    if new_name[len(new_name) - EXTENSION_OFFSET] == " ":
        del (new_name[len(new_name) - EXTENSION_OFFSET])

    episode_name = "".join(new_name)

    for i in range (len(new_name) - EXTENSION_OFFSET):
        if new_name[len(new_name) - EXTENSION_OFFSET].isalpha():
            break
        else:
            del (new_name[len(new_name) - EXTENSION_OFFSET])

    for i in range (4):
        del (new_name[len(new_name) - 1])
            
    folder_name = "".join(new_name)
    directory = series_path + folder_name 

    if os.path.exists(series_path + folder_name):
        newPath = shutil.copy(name, directory + path_separator + episode_name)
        sleep (5)

        os.remove(download_path + path_separator + name)
    else:
        try:
            os.mkdir (directory)    
            newPath = shutil.copy(name, directory + path_separator + episode_name)
            sleep (5)

            os.remove(download_path + path_separator + name)
        except  OSError:
            print ('Cagacion')
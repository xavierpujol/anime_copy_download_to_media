import os
import shutil

from time import sleep

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

    # file_size =  os.path.getsize (download_path + path_separator + name)
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

            # copied_file_size = 0

            # print ('starting copy')
            
            # seconds = 0

            # while copied_file_size < file_size:
            #     sleep (2)
            #     copied_file_size = os.path.getsize (directory + path_separator + episode_name)
            #     seconds += 2
            #     print (str(seconds) + "have gone")

            # print ('end copy')

        except  OSError:
            print ('Cagacion')
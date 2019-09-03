import os
import shutil
#The path of the directory which contains clutter to be organized
#modules required for base opertions
import os
import shutil
#modules for interface creation
from tkinter import filedialog
from tkinter import *
from colorama import Fore, Back, Style
import time
 #modules for command line interface
from colorama import init 
from termcolor import colored 

init() 
  
print(Fore.GREEN + Style.BRIGHT + " #####                                                       #     #                                           \n"
"#     #  #      #    # ##### ##### ###### #####              ##   ##   ##   #    #   ##    ####  ###### #####  \n"
"#        #      #    #   #     #   #      #    #             # # # #  #  #  ##   #  #  #  #    # #      #    # \n"
"#        #      #    #   #     #   #####  #    #    #####    #  #  # #    # # #  # #    # #      #####  #    # \n"
"#        #      #    #   #     #   #      #####              #     # ###### #  # # ###### #  ### #      #####  \n"
"#     #  #      #    #   #     #   #      #   #              #     # #    # #   ## #    # #    # #      #   #  \n"
" #####   #####   ####    #     #   ###### #    #             #     # #    # #    # #    #  ####  ###### #    # \n")

print(Fore.RED + 'Select the Folder you want to make clutter free!') 

time.sleep(2)
def get_folder():
    # Allow user to select a directory and store it in global variable called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    return filename

root = Tk()
root.withdraw()
folder_path = StringVar()
#The path of the directory which contains clutter to be organized
dir_path = get_folder()
print(dir_path)

#list_files contains individual files/directories in the source directory
list_files = os.listdir(dir_path)
for file in list_files:
    #Iterating through each file in the directory
    if not os.path.isdir(dir_path+'\\'+file):\
        #checking if it is a sub-directory
        try:
            extension = file.split('.')[-1]
            #splitting the extension from the file name
            target_folder = dir_path+'\\'+extension+' files'
            if target_folder not in list_files:
                #checking if the a that certain target directory exits in the source
                list_files.append(target_folder)
                os.mkdir(target_folder)
                #creating new directory
            #setting things for moving files
            src_file = os.path.join(dir_path, file)
            dst_file = os.path.join(target_folder, file)
            shutil.move(src_file, dst_file)
            #file moved
        except:
            pass
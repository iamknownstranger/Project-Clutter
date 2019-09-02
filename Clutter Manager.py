import os
import shutil
#The path of the directory which contains clutter to be organized
dir_path = 'D:\Downloads'
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
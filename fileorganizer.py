#Python script for automatically organising files
import os
import shutil

path = input("Enter Path: ")     #enter path of the file you want to organize                
files = os.listdir(path)         #variable files consist of list of files

for file in files:                               #using for loop to traverse each file
    filename,extension = os.path.splitext(file)  #splitting file name and extension of file
    #we only need the extension name so we're removing extras through slicing
    extension = extension[1:]                    

    #if extension directory already exists, we'll move the file to that directory
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    #else we make a new directory and move the file into it
    else: 
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
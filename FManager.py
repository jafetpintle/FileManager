from re import S
import shutil
import os
import ctypes

path_src = r'Files\Documentos'
path_dst = r'Files\Destino'
file_extension = '.jpg'

def move_files(files_names):
    '''
    Function to move files from a directory
    to other directory
    '''
    for file in files_names:
        shutil.move(path_src+'\\'+file, path_dst)
    
def get_files(dir_path: str, ext: str):
    '''
    Funtion to walk across a directory an return
    all the files inside
    '''
    # list to store files
    files = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            if(has_extension(ext, path)):
                files.append(path)
    return files
    
def has_extension(ext: str, file: str)->bool:
    '''
    Check if my file is of a specific extension
    '''
    # this will return a tuple of root and extension
    split_file = os.path.splitext(file)
    #Return true if is the same extension
    return ext == split_file[1] 

def print_files(files):
    for file in files:
        print(f'File: {file}')

def run():
    files = get_files(path_src, file_extension)
    print('You will move the following files: ')
    print_files(files)
    print('-----')
    move_files(files)
    print(f'Files of type {file_extension} has been moved!')

if __name__ == "__main__":
    run()
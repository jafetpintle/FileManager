import shutil
import os
import ctypes

path_src = r'Files\Documentos'
path_dst = r'Files\Destino'

def move_files(files_names):
    '''
    Function to move files from a directory
    to other directory
    '''
    for file in files_names:
        shutil.move(path_src+'\\'+file, path_dst)
    

def get_files(dir_path: str):
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
            files.append(path)
    return files
    


def run():
    files = get_files(path_src)
    move_files(files)
    print('Files has been moved!')

if __name__ == "__main__":
    run()
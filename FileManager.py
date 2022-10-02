import shutil
import os

class FileManager:

    def __init__(self):
        self.source_path = ''
        self.destination_path = ''
        self.extension_file = ''
        self.files = []
    
    def set_source_path(self, src):
        self.source_path = src
    
    def set_destination_path(self, dst):
        self.destination_path = dst

    def move_files(self,files_names):
        '''
        Function to move files from a directory
        to other directory
        '''
        for file in files_names:
            shutil.move(self.source_path+'\\'+file, self.destination_path)
        
    def has_extension(self,ext: str, file: str)->bool:
        '''
        Check if my file is of a specific extension
        '''
        # this will return a tuple of root and extension
        split_file = os.path.splitext(file)
        #Return true if is the same extension
        return ext == split_file[1]

    def get_files(self,dir_path: str, ext: str):
        '''
        Funtion to walk across a directory an return
        all the files inside
        '''
        # list to store files
        files = []

        # Iterate directory
        for path in os.listdir(dir_path):
            # check if is of my file extension
            if(self.has_extension(ext, path)):
                files.append(path)
        self.files = files.copy()

    def print_files(self):
        for file in self.files:
            print(f'File: {file}')
    

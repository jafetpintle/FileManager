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

    def set_extension_file(self, ext):
        ext='.'+ext
        self.extension_file = ext

    def move_files(self):
        '''
        Function to move files from a directory
        to other directory
        '''
        for file in self.files:
            shutil.move(self.source_path+'\\'+file, self.destination_path)
        
    def has_extension(self,ext: str, file: str)->bool:
        '''
        Check if my file is of a specific extension
        '''
        # this will return a tuple of root and extension
        split_file = os.path.splitext(file)
        #Return true if is the same extension
        return ext == split_file[1]

    def set_files(self):
        '''
        Funtion to walk across a directory an return
        all the files inside
        '''
        # list to store files
        files = []

        # Iterate directory
        for path in os.listdir(self.source_path):
            # check if is of my file extension
            if(self.has_extension(self.extension_file, path)):
                files.append(path)
        self.files = files.copy()

    def get_files(self):
        files_str = ''
        for file in self.files:
            files_str+= (f'File: {file}')+'\n'
        return files_str
    

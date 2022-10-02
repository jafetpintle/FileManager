from asyncio.windows_events import NULL
import tkinter as tk
from tkinter import filedialog, messagebox
import FileManager


def select_folder(text, file_manager, type):
    """
    Display a box to select a folder, get the path
    and insert it in the entry widget
    """
    path = filedialog.askdirectory()
    text.delete(0,'end')
    text.insert(0,path)
    #Check if is source of detination path
    if type == 1:
        file_manager.set_source_path(path)
    else:
        file_manager.set_destination_path(path)

def find_files(file_manager, text, ext):
    """
    Search files from the source selected
    and insert them to the text selector
    """
    #Set and check extension file
    ext_file = ext.get()
    if(ext_file != ''):
        file_manager.set_extension_file(ext_file)

        #Find files
        file_manager.set_files()
        if( file_manager.get_files()):
            text.insert(tk.INSERT , file_manager.get_files())
        else:
            messagebox.showwarning(message='No files found', title='Warning!')
    else:
        messagebox.showwarning(message='Type a extension file', title='Warning!')
        ext.focus()

def move_files(file_manager):
    """
    Move files from the source to the destination files
    """
    file_manager.move_files()


class MainApplication(tk.Frame):
    

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        file_manager = FileManager.FileManager()

        colors = {'primary':'#2b2d42', 'secundary':'#d90429', 'text1':'#edf2f4'}

        self['background'] = colors['primary']
        #Def widgets fonts
        font_button =  ('Trebuchet MS', 15)
        font_label = ('Trebuchet MS', 20)
        font_entry = ('Trebuchet MS', 20)
        font_text = ('Trebuchet MS', 15)
        

        #Source folder
        tk.Label(self, text='Move from: ', font=font_label, fg=colors['text1'], bg=colors['primary']).grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        source_entry = tk.Entry(self, width=35, font=font_entry)
        source_entry.grid(column=1,row=0,sticky=tk.W)
        
        source_buttton = tk.Button(self, text='Select folder', bg=colors['secundary'], fg=colors['text1'], font=font_button, command=lambda: select_folder(source_entry, file_manager, 1))
        source_buttton.grid(column=2,row=0, padx=10, pady=5, sticky=tk.W)
    
        #Destination folder
        tk.Label(self, text='To: ', font=font_label, fg=colors['text1'], bg=colors['primary']).grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
        destination_entry = tk.Entry(self, width=35, font=font_entry)
        destination_entry.grid(column=1, row=1, sticky=tk.W)
        
        destination_button = tk.Button(self, text='Select folder', bg=colors['secundary'], fg=colors['text1'], font=font_button, command=lambda: select_folder(destination_entry, file_manager, 0))
        destination_button.grid(column=2,row=1 , padx=10, pady=5, sticky=tk.W)

        #Type of file
        tk.Label(self, text='Type file: ', font=font_label, fg=colors['text1'], bg=colors['primary']).grid(column=0,row=2, padx=5, pady=5,sticky=tk.W)
        extension = tk.Entry(self, width=5, font=font_entry)
        extension.grid(column=1,row=2, sticky=tk.W)
        tk.Label(self, text='(Eg: jpg, png, pdf, ...) ', font=('Trebuchet MS',10), fg=colors['text1'], bg=colors['primary']).grid(column=1,row=2,padx=80, sticky=tk.W)

        #Files
        tk.Label(self,text='Files: ', font=font_label, fg=colors['text1'], bg=colors['primary']).grid(column=0, row=4, padx=5,pady=5, sticky=tk.NW)
        files = tk.Text(self, height=15, width=50,  font=font_text)
        scroll = tk.Scrollbar(self, orient='vertical', command=files.yview)
        files['yscrollcommand'] = scroll.set
        files.grid(column=1, row=4, pady=10, sticky=tk.W)
        scroll.grid(column=1, row=4, pady=10, sticky="nse")

        #Find and move buttons
        tk.Button(self, text='Move files', bg=colors['secundary'], fg=colors['text1'], font=font_button, width=11, command=lambda: move_files(file_manager)).grid(column=2, row=4, padx=10,pady=70, sticky=tk.NE)
        tk.Button(self, text='Find files', bg=colors['secundary'], fg=colors['text1'], font=font_button,width=11, command=lambda: find_files(file_manager, files, extension)).grid(column=2,row=4, padx=10, sticky=tk.NE)

        

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Mafy')
    root.eval('tk::PlaceWindow . center')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
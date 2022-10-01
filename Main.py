import tkinter as tk
from tkinter import filedialog


def selec_folder(text):
    """
    Display a box to select a folder and get the path
    and insert the text in the entry widget
    """
    text.delete(0,'end')
    text.insert(0,filedialog.askdirectory())


class MainApplication(tk.Frame):
    

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        colors = {'primary':'#2b2d42', 'secundary':'#d90429', 'text1':'#edf2f4'}

        self['background'] = colors['primary']
        #Def button font
        font_button =  ('Trebuchet MS', 15)
        font_label = ('Trebuchet MS', 20)
        font_entry = ('Trebuchet MS', 20)
        font_text = ('Trebuchet MS', 15)
        

        #Source folder
        tk.Label(self, text='Move from: ', font=font_label, fg=colors['text1'], bg=colors['primary']).grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        entry_source = tk.Entry(self, width=35, font=font_entry)
        entry_source.grid(column=1,row=0,sticky=tk.W)
        tk.Button(self, text='Select folder', bg=colors['secundary'], fg=colors['text1'], font=font_button, command=lambda: selec_folder(entry_source)).grid(column=2,row=0, padx=10, pady=5, sticky=tk.W)
    
        #Destination folder
        tk.Label(self, text='To: ', font=font_label, fg=colors['text1'], bg=colors['primary']).grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
        entry_destination = tk.Entry(self, width=35, font=font_entry)
        entry_destination.grid(column=1, row=1, sticky=tk.W)
        tk.Button(self, text='Select folder', bg=colors['secundary'], fg=colors['text1'], font=font_button, command=lambda: selec_folder(entry_destination)).grid(column=2,row=1 , padx=10, pady=5, sticky=tk.W)

        #Extension and move files
        tk.Label(self, text='Type file: ', font=font_label, fg=colors['text1'], bg=colors['primary']).grid(column=0,row=2, padx=5, pady=5,sticky=tk.W)
        extension = tk.Entry(self, width=5, font=font_entry)
        extension.grid(column=1,row=2, sticky=tk.W)

        #Find and move buttons
        tk.Button(self, text='Move files', bg=colors['secundary'], fg=colors['text1'], font=font_button, width=11).grid(column=2, row=4, padx=10,pady=70, sticky=tk.NE)
        tk.Button(self, text='Find files', bg=colors['secundary'], fg=colors['text1'], font=font_button,width=11).grid(column=2,row=4, padx=10, sticky=tk.NE)

        #Files
        tk.Label(self,text='Files: ', font=font_label, fg=colors['text1'], bg=colors['primary']).grid(column=0, row=4, padx=5,pady=5, sticky=tk.NW)
        files = tk.Text(self, height=15, width=50,  font=font_text)
        scroll = tk.Scrollbar(self, orient='vertical', command=files.yview)
        files['yscrollcommand'] = scroll.set
        files.grid(column=1, row=4, pady=10, sticky=tk.W)
        scroll.grid(column=1, row=4, pady=10, sticky="nse")
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Mafy')
    root.eval('tk::PlaceWindow . center')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
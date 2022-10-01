import tkinter as tk
from tkinter import ttk


def create_buttons_frame(container):
    frame = ttk.Frame(container)

    
    #Buttons setup
    ttk.Button(frame, text='Select folder').grid(column=1,row=0 , padx=10, pady=5)
    ttk.Button(frame, text='Select folder').grid(column=1,row=1, padx=10, pady=5)

    return frame

def create_input_frame(container):
    frame = ttk.Frame(container)
    #grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    #Source folder
    

    #Destination folder


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


        

        #Source folder
        ttk.Label(self, text='Source: ').grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        entry_source = ttk.Entry(self, width=35)
        entry_source.grid(column=1,row=0,sticky=tk.W)
        ttk.Button(self, text='Select folder').grid(column=2,row=1, padx=10, pady=5, sticky=tk.W)

        #Destination folder
        ttk.Label(self, text='Destination: ').grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
        destinarion_source = ttk.Entry(self, width=35)
        destinarion_source.grid(column=1, row=1, sticky=tk.W)
        ttk.Button(self, text='Select folder').grid(column=2,row=0 , padx=10, pady=5, sticky=tk.W)

        #Extension and move files
        ttk.Label(self, text='Extension: ').grid(column=0,row=2, padx=5, pady=5,sticky=tk.W)
        extension = ttk.Entry(self, width=5)
        extension.grid(column=1,row=2, sticky=tk.W)

        #Find and move buttons
        ttk.Button(self, text='Move files').grid(column=2, row=4, padx=10,pady=40, sticky=tk.NE)
        ttk.Button(self, text='Find files').grid(column=2,row=4, padx=10, sticky=tk.NE)

        #Files
        ttk.Label(self,text='Files: ').grid(column=0, row=4, padx=5,pady=5, sticky=tk.NW)
        files = tk.Text(self, height=15, width=30)
        scroll = ttk.Scrollbar(self, orient='vertical', command=files.yview)
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
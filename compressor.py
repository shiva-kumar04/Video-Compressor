from Tkinter import *
import tkFileDialog as filedialog
import subprocess

master = Tk()

def callback():
    explorer_window = Tk().withdraw()
    file_path = filedialog.askopenfilename()
    input_path.insert(0, file_path)
    return file_path

if __name__ == '__main__':
    master.minsize(400,200)
    Label(master, text='Input file', width=10, height=3).grid(row=0)
    Label(master, text='Target \n File size', width=10, height=3).grid(row=1)
    input_path = Entry(master)
    input_path.grid(row=0, column=1, padx=3)
    b = Button(master, text='Browse',height=1, command=callback)
    b.grid(row=0, column=3)
    mainloop()

from Tkinter import *
import tkFileDialog as filedialog
import subprocess

master = Tk()

def callback():
    explorer_window = Tk().withdraw()
    file_path = filedialog.askopenfilename()
    window.insert(0, file_path)
    global input_path
    input_path = file_path
    print 'CAllback: ',input_path

def compress():
    print 'Compress:', input_path
    if input_path != 'NULL':
        output_path = input_path.split('.')[0] + '_compressed.mp4'
        ffmpeg_cmd = 'ffmpeg -i ' + input_path + ' -fs 15M '+ output_path
        print ffmpeg_cmd
        subprocess.call(ffmpeg_cmd)
    else:
        print 'Choose a file'
if __name__ == '__main__':
    master.minsize(400,200)
    Label(master, text='Input file', width=10, height=3).grid(row=0)
    Label(master, text='Target \n File size', width=10, height=3).grid(row=1)
    window = Entry(master)
    window.grid(row=0, column=1, padx=3)
    browse = Button(master, text='Browse',height=1, command=callback)
    browse.grid(row=0, column=3)
    comp = Button(master, text='Compress', height=1, command=compress)
    comp.grid(row=0, column=4)
    mainloop()

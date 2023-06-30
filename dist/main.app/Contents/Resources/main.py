import time
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import os
from tkinter import filedialog
from threading import Thread

root = Tk() 
root.geometry("120x200")

frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("P2I")

lbl = Label(frm)
lb2 = Label(frm)
lb3 = Label(frm)

pb =    ttk.Progressbar(
        frm,
        orient='horizontal',
        mode='determinate',
        length=70

        )

def icon2():
    name = filedialog.askopenfilename()
    lb2.config(text=name)
    name2=name.rfind('/') + 1
    name3=f'{name[name2:]}'
    lb3.config(text=name3)

def icon():
    pb.start(1)
    Thread(target=icon3).start()
    
def icon3():
    time.sleep(3)
    file1 = lb2.cget("text")
    os.system(f"generate-iconset --use-sips {file1}")
    pb.stop()
    Label(frm, text="done!").grid(column=1, row=4)
  
if __name__ == "__main__":
    ttk.Button(frm, text="Convert", command=icon).grid(column=1, row=2)
    ttk.Button(frm, text="Select File", command=icon2).grid(column=1, row=0)
    lb3.grid(column=1, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
    pb.grid(column=0, row=3, columnspan=2, padx=10, pady=20 )

    root.mainloop()


from fileinput import filename
import tkinter
from tkinter import filedialog
from tkinter import colorchooser

window = tkinter.Tk()

# abre una ventana para seleccionar un archivo
filename = filedialog.askopenfilename()

# abre una ventana para seleccionar un color
colorchooser.askcolor(initialcolor='#ffffff')

window.mainloop()

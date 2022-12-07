# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener
# una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter
from tkinter import ttk, StringVar

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Elemento 1", value=1, variable=selected)
r2 = ttk.Radiobutton(window, text="Elemento 2", value=2, variable=selected)
r3 = ttk.Radiobutton(window, text="Elemento 3", value=3, variable=selected)

r1.grid(row=1, column=0, pady=5, padx=5)
r2.grid(row=2, column=0, pady=5, padx=5)
r3.grid(row=3, column=0, pady=5, padx=5)


label1 = tkinter.Label(text="Etiqueta!", bg="blue", fg="yellow")
label1.grid(ipadx=50, ipady=20)


window.mainloop()

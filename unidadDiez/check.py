import tkinter
from tkinter import ttk

window = tkinter.Tk()


def miFuncion():
    print("Clickado")  # command

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()
checkbox = ttk.Checkbutton(window, text="Acepto",
                           variable=selected, command=miFuncion)
# command le da funcionalidad al checkbox

checkbox.grid(column=0, row=0, sticky='nsew')


window.mainloop()

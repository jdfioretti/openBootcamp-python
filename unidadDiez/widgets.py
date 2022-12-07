import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Si", value=1, variable=selected)
r2 = ttk.Radiobutton(window, text="No", value=2, variable=selected)
r3 = ttk.Radiobutton(window, text="Quiza", value=3, variable=selected)

#selected agrupa todos los elementos que hay dentro, y solo se puede elegir uno

r1.grid(row=1, column=0, pady=5, padx=5)
r2.grid(row=2, column=0, pady=5, padx=5)
r3.grid(row=3, column=0, pady=5, padx=5)

#se pueden crear otros grupos de variables

selected2 = tkinter.StringVar()
rs1 = ttk.Radiobutton(window, text="Si-2", value=1, variable=selected2)
rs1.grid(row=0, column=1, pady=5, padx=5)


window.mainloop()

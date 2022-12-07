from cProfile import label
import random
import tkinter
from tkinter import ttk

window = tkinter.Tk()

colors = ["red", "green", "blue", "yellow", "orange", "purple"]

for x in range(0, 10):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)

    ancho = random.randint(0, 50)
    alto = random.randint(0, 100)

    label = tkinter.Label(window, text='Etiqueta!',
                          bg=colors[color], fg=colors[color2])
    label.place(x=random.randint(0, 100), y=random.randint(0, 100))

window.mainloop()
sys.exit(0)

label1 = tkinter.Label(
    window, text="Posicionamiento abosoluto", bg="blue", fg='white')
label1.place(x=10, y=50)

label2 = tkinter.Label(
    window, text="Otro más", bg="red", fg='yellow')
label2.place(relx=0.10, rely=0.15, relwidth=0.5, anchor='ne')



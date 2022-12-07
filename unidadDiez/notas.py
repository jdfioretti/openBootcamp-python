from cProfile import label
import pprint
from pprint import pprint
import tkinter
from tkinter.ttk import LabelFrame

# para empezar a utilizar nuestro tkinter debemos tener algo donde poner los componentes/widgets:
# botones, input, cajas, etiquetas, etc --> dentro de un contenedor
# creamos una ventana

window = tkinter.Tk()  # creamos una instancia de tk
# print(type(window))

# pprint.pprint(dir(window))  # para ver los metodos disponibles

label_saludo = tkinter.Label(window, text="Hola mundo", bg='yellow', fg='blue')
label_saludo.pack(ipadx=50, ipady=50, expand=True)

label_adios = tkinter.Label(window, text="Adios mundo", bg='red', fg='white')
label_adios.pack(fill='both', expand=True)


window.mainloop()   # para abrir la ventana
# window.destroy()   # para cerrar la ventana
    
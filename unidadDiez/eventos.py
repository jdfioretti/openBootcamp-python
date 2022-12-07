import tkinter

window = tkinter.Tk()


def salir(event):
    print('Adios')
    window.quit()


def saludar(event):
    print('Han hecho click en saludar')


def saludarDoble(event):
    print('Han hecho doble click')


boton = tkinter.Button(window, text="Haz Click!")
boton.pack()
boton.bind("<Button-1>", saludar)
boton.bind("<Double-1>", saludarDoble)

botonSalir = tkinter.Button(window, text="Salir!")
botonSalir.pack()
botonSalir.bind("<Button-1>", salir)


window.mainloop()

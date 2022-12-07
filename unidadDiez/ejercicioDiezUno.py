from tkinter import Tk, StringVar, Radiobutton, Button, W

options = ['Opción 1', 'Opción 2', 'Opción 3', 'Opción 4']
window = Tk()
window.geometry('220x150')
window.columnconfigure(1, weight=1)
window.columnconfigure(3, weight=1)
window.title('Select..')
var = StringVar()
var.set(0)


def reinicio():
    var.set(0)
    window.title('Select..')


def selected():
    window.title(f'{var.get()}')


for i in range(0, len(options)):
    Radiobutton(window, text=options[i], variable=var,
                value=options[i], command=selected).grid(padx=0, row=i, column=0, sticky=W)

Button(window, text="Resetear", command=reinicio, width=15,
       height=5).grid(column=2, row=0, rowspan=5)

window.mainloop()

import tkinter
from tkinter import Label, ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Usuario
# Etiqueta usuario
username_label = ttk.Label(window, text="Username:")
username_label.grid(row=0, column=0, sticky=tkinter.W, padx=5, pady=5)

# Campo usuario
username_entry = ttk.Entry(window, width=30)
username_entry.grid(row=0, column=1, sticky=tkinter.E, padx=5, pady=5)

# Etiqueta contraseña
password_label = ttk.Label(window, text="Password:")
password_label.grid(row=1, column=0, sticky=tkinter.W, padx=5, pady=5)

# Campo contraseña
username_entry = ttk.Entry(window, width=30, show='*')
username_entry.grid(row=1, column=1, sticky=tkinter.E, padx=5, pady=5)

# Boton
# Etiqueta boton

login_button = ttk.Button(window, text="Login")
login_button.grid(row=3, column=1, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()

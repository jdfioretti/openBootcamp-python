import tkinter

window = tkinter.Tk()

label1 = tkinter.Label(text="label1", bg="red", fg="white")
label1.pack(ipadx=45, ipady=15, fill='x')

label2 = tkinter.Label(text="label2", bg="blue", fg="yellow")
label2.pack(ipadx=45, ipady=15, fill='x')

label3 = tkinter.Label(text="label3", bg="green", fg="grey")
label3.pack(ipadx=45, ipady=15, fill='x')

label4 = tkinter.Label(text="label4", bg="purple", fg="white")
label4.pack(ipadx=15, ipady=15, side='left')

label5 = tkinter.Label(text="label5", bg="black", fg="white")
label5.pack(ipadx=15, ipady=15, side='left')

label6 = tkinter.Label(text="label6", bg="white", fg="black")
label6.pack(ipadx=15, ipady=15)

window.mainloop()

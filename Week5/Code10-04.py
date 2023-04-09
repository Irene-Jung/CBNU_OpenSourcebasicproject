from tkinter import *

window = Tk()

photo = PhotoImage(file = "dog.gif")
label1 = Label(window, image = photo)

label1.pack(side = LEFT)

window.mainloop()

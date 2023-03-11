from tkinter import *

root = Tk()
root.geometry('500x300')
root.title('KeyBoard Event')


def action(event):
    label = Label(root, text=f"Bạn vừa nhấn phím có char là: {event.char} và có keysym: {event.keysym}")
    label.pack()


root.bind("<a>", action)

root.mainloop()




















# if event.keysym == "Return":
#     label = Label(root, text=f"Bạn vừa nhấn phím Enter")
#     label.pack()
# elif event.keysym == "a":
#     label = Label(root, text=f"Bạn vừa nhấn phím a")
#     label.pack()
from tkinter import *

root = Tk()
root.geometry('400x400')

def changeWord(word):
    label_show.config(text=word)

label_show = Label(root)

button_bye = Button(
    root, 
    text="Tạm biệt", 
    command=lambda: changeWord("Tạm biệt các bạn nhé")
)

button_hi = Button(
    root, 
    text="Xin chào", 
    command=lambda: changeWord("Xin chào các bạn nhé")
)

label_show.pack()
button_bye.pack()
button_hi.pack()

root.mainloop()

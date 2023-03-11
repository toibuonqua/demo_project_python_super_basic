from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Event')

def show(event):
    label = Label(root, text='Bạn vừa nhấn vào' + str(event.x) + ' ' + str(event.y))
    label.pack()
    

button = Button(root, text='Click!')
button.bind("<Button-1>", show)
button.pack()

root.mainloop()
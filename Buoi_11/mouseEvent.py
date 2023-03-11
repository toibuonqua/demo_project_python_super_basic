from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Mouse Event')

def enter(event):
    label = Label(root, text=f"Bạn vừa trỏ vào nút")
    label.pack()

def leave(event):
    label = Label(root, text=f"Bạn vừa trỏ ra ngoài nút")
    label.pack()

def button1(event):
    label = Label(root, text=f"Bạn vừa nhấn chuột trái")
    label.pack()

def button3(event):
    label = Label(root, text=f"Bạn vừa nhấn chuột phải")
    label.pack()

def button2(event):
    label = Label(root, text=f"Bạn vừa nhấn chuột giữa")
    label.pack()

def button4(event):
    label = Label(root, text=f"Bạn vừa lăn chuột lên trên")
    label.pack()

def button5(event):
    label = Label(root, text=f"Bạn vừa lăn chuột xuống dưới")
    label.pack()

def action(event):
    label = Label(root, text=f"Bạn đang di chuyển chuột trong màn hình root")
    label.pack()



root.bind("<Enter>", enter)
root.bind("<Leave>", leave)
root.bind("<Button-1>", button1)
root.bind("<Button-2>", button2)
root.bind("<Button-3>", button3)
root.bind("<Button-4>", button4)
root.bind("<Button-5>", button5)
root.bind("<Motion>", action)

root.mainloop()
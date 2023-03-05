from tkinter import *

root = Tk()
root.geometry('800x800')
new_frame = Frame(root, height=400, width=400)
new_frame2 = Frame(root, height=400, width=400, bg='red')

def action():
    new_frame2.after(500, show)

def show():
    global id_action
    label_show.config(text="chào cac bạn")
    id_action = new_frame2.after(500, hide)
    print(id_action)
    
def hide():
    global id_action
    label_show.config(text="")
    id_action = new_frame2.after(500, show)
    print(id_action)

def stop_action():
    print(new_frame2.after_cancel(id_action))

label_show = Label(new_frame, text="")
button_act = Button(new_frame, text="click", command=action)    
button_stop_act = Button(new_frame, text="stop", command=stop_action)

new_frame.pack(expand=1, fill=BOTH)
new_frame2.pack(expand=1, fill=BOTH)

label_show.pack()
button_act.pack()
button_stop_act.pack()

root.mainloop()
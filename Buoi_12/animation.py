from tkinter import *
from mario_character import mario_character
from map_loading import map_loading

# Thiết lập màn hình giao diện chính
root = Tk()
root.geometry('800x700')
root.title('Mario Move')


# Khởi tạo tiện ích canvas
my_canvas = Canvas(root, width=800, height=700)
my_canvas.pack(fill=BOTH, expand=True)


# Khởi tạo nhân vật và màn chơi
mario = mario_character()
map = map_loading()
interface = 300


# Các hàm chức năng
def keyEvent(event):
    print(event.keysym)
    if event.keysym == "Right":
        animationWidget('run')
    if event.keysym == "Left":
        stop()
    if event.keysym == "Up":
        print("interface", interface)
        if interface == 300:
            if code_fall:
                root.after_cancel(code_fall)
            animationWidget('jump')
    return

def fall():
    global interface, code_fall
    if interface < 300:
        label_char.place(y=interface, x=350)
        interface += 10
        code_fall = root.after(60, fall)
    print(interface)

def animationWidget(action):
    global ma_run_after, interface, code_up
    if action == 'run':
        changeImage(mario.run(), map.next_frame())
        ma_run_after = root.after(60, lambda: animationWidget(action))
    if action == 'jump':
        if interface > 200:
            label_char.place(y=interface, x=350)
            interface -= 10
            code_up = root.after(60, lambda: animationWidget(action))
        else:
            fall()
        print(interface)
    return 0

def stop():
    root.after_cancel(ma_run_after)


def changeImage(charIma, mapIma):
    label_char.config(image=charIma)
    label_bg.config(image=mapIma)


# Khởi tạo các tiện ích trên màn hình chính
label_bg = Label(root, image=map.list_frame[0])
label_char = Label(root, image=mario.list_run[0], bg='#5e91fe')
button_run = Button(root, text="Chạy", command=lambda: animationWidget('run'))
button_jump = Button(root, text="Nhảy", command=lambda: animationWidget('jump'))
button_stop = Button(root, text="Dừng lại", command=stop)


# Dàn các tiện ích trên màn hình
canvas_label_bg = my_canvas.create_window(10, 0, anchor="nw", window=label_bg)
canvas_label_char = my_canvas.create_window(350, 300, anchor="nw", window=label_char)
canvas_button_run = my_canvas.create_window(400, 550, anchor="nw", window=button_run)
canvas_button_jump = my_canvas.create_window(300, 550, anchor="nw", window=button_jump)
canvas_button_stop = my_canvas.create_window(200, 550, anchor="nw", window=button_stop)

# label_bg.place(y=0, x=10)
# label_char.place(y=300, x=350)
# button_run.pack(side=RIGHT, fill=X)
# button_jump.pack(fill=X)
# button_stop.pack(side=LEFT, fill=X)

root.bind("<Key>", keyEvent)

root.mainloop()
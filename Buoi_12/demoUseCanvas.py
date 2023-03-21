from tkinter import *
from mario_characer import mario_character
from map_loading import map_loading

# Thiết lập màn hình giao diện chính
root = Tk()
root.geometry('800x700')
root.title('Mario Move')


# Khởi tạo tiện ích canvas
my_canvas = Canvas(root, width=800, height=600)


# Khởi tạo frame
my_frame = Frame(root)


# Khởi tạo nhân vật và màn chơi
mario = mario_character()
map = map_loading()
charPosiX = 350
charPosiY = 300
currentCharIma = mario.list_run[0]
currentMapIma = map.list_frame[0]
ground = True


# Các hàm chức năng
def keyEvent(event):
    print(event.keysym)
    if event.keysym == "Right":
        animationWidget(actionRun=True)
    if event.keysym == "Left":
        stop()
    if event.keysym == "Up":
        print("Không thực hiện nhảy trên không được", charPosiY)
        if ground == True:
            animationWidget(actionJump=True)
    return

def fall():
    global charPosiY, code_fall, ground
    if charPosiY < 300:
        changeImage(currentCharIma, currentMapIma, [charPosiX, charPosiY])
        charPosiY += 10
        code_fall = root.after(40, fall)
    else:
        ground = True
        print(ground)
    print(charPosiY)
    return 'fall'

def animationWidget(actionRun=False, actionJump=False):
    global ma_run_after, charPosiY, currentCharIma, currentMapIma, ground
    if actionRun:
        currentCharIma = mario.run()
        currentMapIma = map.next_frame()
        changeImage(currentCharIma, currentMapIma, [charPosiX, charPosiY])
        ma_run_after = root.after(40, lambda: animationWidget(actionRun=True))
    if actionJump:
        if charPosiY > 200:
            changeImage(currentCharIma, currentMapIma, [charPosiX, charPosiY])
            charPosiY -= 10
            ground = False
            root.after(40, lambda: animationWidget(actionJump=True))
        else:
            print(ground)
            fall()
        print(charPosiY)
    return 'animation'

def stop():
    root.after_cancel(ma_run_after)
    return 'stop'


def changeImage(charIma, mapIma, charPositon=[350, 300]):
    my_canvas.delete('all')
    my_canvas.create_image(10, 0, anchor="nw",image=mapIma)
    my_canvas.create_image(charPositon[0], charPositon[1], anchor="nw", image=charIma)
    return 'render display'


# Khởi tạo các tiện ích trên màn hình chính
my_canvas.create_image(10, 0, anchor="nw",image=currentMapIma)
my_canvas.create_image(350, 300, anchor="nw", image=currentCharIma)
# label_bg = Label(root, image=map.list_frame[0])
# label_char = Label(root, image=mario.list_run[0], bg='#5e91fe')
button_run = Button(my_frame, text="Chạy", command=lambda: animationWidget(actionRun=True))
button_jump = Button(my_frame, text="Nhảy", command=lambda: animationWidget(actionJump=True))
button_stop = Button(my_frame, text="Dừng lại", command=stop)


# Dàn các tiện ích trên màn hình
# canvas_label_bg = my_canvas.create_window(10, 0, anchor="nw", window=label_bg)
# canvas_label_char = my_canvas.create_window(350, 300, anchor="nw", window=label_char)
# canvas_button_run = my_canvas.create_window(450, 550, anchor="nw", window=button_run)
# canvas_button_jump = my_canvas.create_window(350, 550, anchor="nw", window=button_jump)
# canvas_button_stop = my_canvas.create_window(250, 550, anchor="nw", window=button_stop)

# label_bg.place(y=0, x=10)
# label_char.place(y=300, x=350)
button_run.grid(row=0, column=2)
button_jump.grid(row=0, column=1)
button_stop.grid(row=0, column=0)


# event ấn keyboard
root.bind("<Key>", keyEvent)


# Dàn bố cục màn hình
my_canvas.pack()
my_frame.pack()


# mainloop
root.mainloop()
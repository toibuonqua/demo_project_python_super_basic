from tkinter import *
from threading import Timer
from mario_characer import mario_character
from map_loading import map_loading

root = Tk()
root.geometry('800x600')
root.title('Mario Move')

mario = mario_character()
map = map_loading()

def animationWidget(index, action):
    if action == 'run':
        if index < len(mario.list_run):
            changeImage(mario.run(), map.next_frame())
            index += 1
            root.after(80, lambda: animationWidget(index, action))
    if action == 'rush':
        if index < len(mario.list_rush):
            changeImage(mario.rush(), map.next_frame())
            index += 1
            root.after(80, lambda: animationWidget(index, action))
    return 0
        

def changeImage(charIma, mapIma):
    label_1.config(image=charIma)
    label_bg.config(image=mapIma)


label_bg = Label(root, image=map.list_frame[0])
label_1 = Label(root, image=mario.list_run[0])
button_1 = Button(root, text="Chạy", command=lambda: animationWidget(0, 'run'))
button_2 = Button(root, text="Chạy nhanh", command=lambda: animationWidget(0, 'rush'))


label_bg.place(y=0, x=10)
label_1.place(y=300, x=350)
button_1.place(y=550, x=400)
button_2.place(y=550, x=300)

root.mainloop()
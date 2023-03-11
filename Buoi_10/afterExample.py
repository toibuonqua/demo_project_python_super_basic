from tkinter import *

root = Tk()
root.geometry('600x400')

anh_nhan_vat = [
    PhotoImage(file="image/ima_not_bg/mario_run_1.png").subsample(1),
    PhotoImage(file="image/ima_not_bg/mario_run_2.png").subsample(1),
    PhotoImage(file="image/ima_not_bg/mario_run_3.png").subsample(1),
    PhotoImage(file="image/ima_not_bg/mario_run_4.png").subsample(1),
    PhotoImage(file="image/ima_not_bg/mario_run_5.png").subsample(1),
    PhotoImage(file="image/ima_not_bg/mario_run_6.png").subsample(1),
]
number_stop = len(anh_nhan_vat)
chi_muc = 0
x_ban_dau = 0
y_ban_dau = 0

def changeWord():
    
    global chi_muc, number_stop, ma_after, x_ban_dau
    if chi_muc < number_stop:
        label_show.config(image=anh_nhan_vat[chi_muc])
        x_ban_dau = x_ban_dau + 10
        label_show.place(y=0, x=x_ban_dau)
        chi_muc = chi_muc + 1
        if chi_muc == number_stop:
            chi_muc = 0
        ma_after = root.after(100, changeWord)
        print(ma_after)

def stop():
    root.after_cancel(ma_after)

label_show = Label(root, image=anh_nhan_vat[0])
button_action = Button(
    root, 
    text="Chạy chương trình", 
    command=changeWord
)
button_stop = Button(
    root, 
    text="Dừng chương trình", 
    command=stop
)

label_show.place(y=0, x=0)
button_action.place(y=200, x=150)
button_stop.place(y=200, x=350)

root.mainloop()
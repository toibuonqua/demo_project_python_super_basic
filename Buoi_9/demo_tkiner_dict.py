from tkinter import *
from threading import Timer
import time


root = Tk()
root.geometry("500x500")
root.title("Tra cứu điểm của học sinh")


# create widget
new_entry = Entry(root)
new_button = Button(root, text='Tìm kiếm', command=lambda:search(new_entry.get()))
label_notice = Label(root)
label_result = Label(root)


# data to check
dict_student_point = {
    'Nam': 10,
    'Hoàng': 9,
    'Đạt': 8,
    'Long': 5,
    'Quang': 7,
    'Tú': 6,
    'Quân': 4,
    'Dương': 9,
    'Đức': 2,
    'Trọng': 7,
    'Việt': 10,
}


# function 
def search(word):
    
    notice_down = Timer(5.0, shut_down_notice)
    
    if word == '':
        label_notice.config(text="Không có từ khóa để tìm kiếm")
        notice_down.start()
        return
      
    search_word = (word.lower()).title()
    if search_word in dict_student_point:
        label_result.config(text=f"Bạn {search_word} có số điểm là: {dict_student_point[search_word]}")
        return
    
    label_notice.config(text="Không có học sinh trong danh sách")
    notice_down.start()
    return
     
     
def shut_down_notice():
    label_notice.config(text="")


# helper



# layout for widget
label_notice.pack()
new_entry.pack()
new_button.pack()
label_result.pack()

root.mainloop()
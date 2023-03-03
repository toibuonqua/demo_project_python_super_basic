from tkinter import *

class map_loading:
    
    def __init__(self):
        self.list_frame = [
            PhotoImage(file="image/map_screen_1.png").subsample(1),
            PhotoImage(file="image/map_screen_2.png").subsample(1),
            PhotoImage(file="image/map_screen_3.png").subsample(1),
            PhotoImage(file="image/map_screen_4.png").subsample(1),
            PhotoImage(file="image/map_screen_5.png").subsample(1),
            PhotoImage(file="image/map_screen_6.png").subsample(1),
            PhotoImage(file="image/map_screen_7.png").subsample(1),
            PhotoImage(file="image/map_screen_8.png").subsample(1),
            PhotoImage(file="image/map_screen_9.png").subsample(1),
            PhotoImage(file="image/map_screen_10.png").subsample(1),
            PhotoImage(file="image/map_screen_11.png").subsample(1),
            PhotoImage(file="image/map_screen_12.png").subsample(1),
            PhotoImage(file="image/map_screen_13.png").subsample(1),
            PhotoImage(file="image/map_screen_14.png").subsample(1),
            PhotoImage(file="image/map_screen_15.png").subsample(1),
            PhotoImage(file="image/map_screen_16.png").subsample(1),
            PhotoImage(file="image/map_screen_17.png").subsample(1),
            PhotoImage(file="image/map_screen_18.png").subsample(1),
            PhotoImage(file="image/map_screen_19.png").subsample(1),
            PhotoImage(file="image/map_screen_20.png").subsample(1),
            PhotoImage(file="image/map_screen_21.png").subsample(1),
            PhotoImage(file="image/map_screen_22.png").subsample(1),
            PhotoImage(file="image/map_screen_23.png").subsample(1),
            PhotoImage(file="image/map_screen_24.png").subsample(1),
            PhotoImage(file="image/map_screen_25.png").subsample(1),
            PhotoImage(file="image/map_screen_26.png").subsample(1),
            PhotoImage(file="image/map_screen_27.png").subsample(1),
            PhotoImage(file="image/map_screen_28.png").subsample(1),
            PhotoImage(file="image/map_screen_29.png").subsample(1),
            PhotoImage(file="image/map_screen_30.png").subsample(1),
            PhotoImage(file="image/map_screen_31.png").subsample(1),
        ]
        self.index_frame = 0
    
    def next_frame(self):
        index = self.index_frame
        self.index_frame += 1
        if self.index_frame == len(self.list_frame):
            self.index_frame = 0
        return self.list_frame[index]

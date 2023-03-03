from tkinter import *
from PIL import ImageTk, Image

class mario_character:
    
    def __init__(self):
        self.list_run = [
            # ImageTk.PhotoImage(Image.open('image/ima_not_bg/mario_run_1.png')),
            PhotoImage(file="image/ima_not_bg/mario_run_1.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_run_2.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_run_3.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_run_4.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_run_5.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_run_6.png").subsample(1),
        ]
        self.list_stop = [
            PhotoImage(file="image/ima_not_bg/mario_stop_1.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_stop_2.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_stop_3.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_stop_4.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_stop_5.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_stop_6.png").subsample(1),
        ]
        self.list_rush = [
            PhotoImage(file="image/ima_not_bg/mario_rush_1.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_rush_2.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_rush_3.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_rush_4.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_rush_5.png").subsample(1),
            PhotoImage(file="image/ima_not_bg/mario_rush_6.png").subsample(1),
        ]
        self.run_action = 0
        self.stop_action = 0
        self.rush_action = 0
    
    def run(self):
        action = self.run_action
        self.run_action += 1
        if self.run_action == len(self.list_run):
            self.run_action = 0
        return self.list_run[action]
    
    def stop(self):
        action = self.stop_action
        self.stop_action += 1
        if self.stop_action == len(self.list_stop):
            self.stop_action = 0
        return self.list_stop[action]
    
    def rush(self):
        action = self.rush_action
        self.rush_action += 1
        if self.rush_action == len(self.list_rush):
            self.rush_action = 0
        return self.list_rush[action]
    
    
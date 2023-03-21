from tkinter import *

root = Tk()

background_image = PhotoImage(file="image/map_screen_1.png")

C = Canvas(root, height=800, width=1000)

filename = PhotoImage(file="image/ima_not_bg/mario_run_1.png")
filename2 = PhotoImage(file="image/ima_not_bg/mario_run_2.png")
image = C.create_image(500, 300, image=background_image)
char = C.create_image(500, 430, image=filename)

# C = Canvas(root, height=800, width=1000)
# char = C.create_image(500, 430, image=filename2)

C.pack(fill=BOTH, expand=1)
root.mainloop()
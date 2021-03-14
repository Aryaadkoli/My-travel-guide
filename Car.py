from tkinter import *
from PIL import ImageTk, Image

win1 = Tk()
win1.title("Road Tours")
win1.geometry('960x570+0+0')
win1.resizable(0, 0)

my_img1 = ImageTk.PhotoImage(Image.open("D:/Img/Road-1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("D:/Img/Road-2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("D:/Img/Road-3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("D:/Img/Road-4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("D:/Img/Road-5.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(win1, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(win1, text="<<", command=lambda: forward(image_number - 1))

    if image_number == 5:
        button_forward = Button(win1, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number + 1])
    button_forward = Button(win1, text=">>", command=lambda: forward(image_number - 1))
    button_back = Button(win1, text="<<", command=lambda: forward(image_number + 1))

    if image_number == 1:
        button_back = Button(win1, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(win1, text="<<", command=back, state=DISABLED)
button_exit = Button(win1, text="Exit Program", command=win1.quit)
button_forward = Button(win1, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

win1.mainloop()

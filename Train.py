from tkinter import *
from PIL import ImageTk, Image

win2 = Tk()
win2.title("Train Tours")
win2.geometry('960x570+0+0')
win2.resizable(0, 0)

my_img1 = ImageTk.PhotoImage(Image.open("D:/Img/Train-1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("D:/Img/Train-2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("D:/Img/Train-3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("D:/Img/Train-4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("D:/Img/Train-5.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(win2, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(win2, text="<<", command=lambda: forward(image_number - 1))

    if image_number == 5:
        button_forward = Button(win2, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number + 1])
    button_forward = Button(win2, text=">>", command=lambda: forward(image_number - 1))
    button_back = Button(win2, text="<<", command=lambda: forward(image_number + 1))

    if image_number == 1:
        button_back = Button(win2, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(win2, text="<<", command=back, state=DISABLED)
button_exit = Button(win2, text="Exit Program", command=win2.quit)
button_forward = Button(win2, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

win2.mainloop()

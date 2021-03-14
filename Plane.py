from tkinter import *
from PIL import ImageTk, Image

win3 = Tk()
win3.title("Airplane Tours")
win3.geometry('960x570+0+0')
win3.resizable(0, 0)

my_img1 = ImageTk.PhotoImage(Image.open("D:/Img/Ajanta ellora.PNG"))
my_img2 = ImageTk.PhotoImage(Image.open("D:/Img/Darjeeling.PNG"))
my_img3 = ImageTk.PhotoImage(Image.open("D:/Img/Elephant beach.PNG"))
my_img4 = ImageTk.PhotoImage(Image.open("D:/Img/gir national park.PNG"))
my_img5 = ImageTk.PhotoImage(Image.open("D:/Img/konark sun temple.PNG"))
my_img6 = ImageTk.PhotoImage(Image.open("D:/Img/taj mahal.PNG"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(win3, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(win3, text="<<", command=lambda: forward(image_number - 1))

    if image_number == 6:
        button_forward = Button(win3, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number + 1])
    button_forward = Button(win3, text=">>", command=lambda: forward(image_number - 1))
    button_back = Button(win3, text="<<", command=lambda: forward(image_number + 1))

    if image_number == 1:
        button_back = Button(win3, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(win3, text="<<", command=back, state=DISABLED)
button_exit = Button(win3, text="Exit Program", command=win3.quit)
button_forward = Button(win3, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

win3.mainloop()
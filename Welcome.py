from tkinter import *
from PIL import ImageTk, Image
from tkinter.tix import *

root = Tk()
root.title('Travel guide')
h = root.winfo_screenheight()  # height of screen of respective computer
w = root.winfo_screenwidth()  # width of screen of respective computer
root.geometry(f"{w}x{h}")  # this defines the geometry of the window
root.resizable(0, 0)  # this is to prevent from resizing the window

# Define image
bg1 = PhotoImage(file='D:/Img/bg3.png')

# Create canvas
my_canvas = Canvas(root, width=w, height=h)
my_canvas.place(x=0, y=0)
# my_canvas.pack(fill='both', expand=True)


def trip():
    root.destroy()
    import Trip
    Trip.win.mainloop()


def car():
    root.destroy()
    import Car
    Car.win1.mainloop()


def train():
    root.destroy()
    import Train
    Train.win2.mainloop()


def plane():
    root.destroy()
    import Plane
    Plane.win3.mainloop()


def bookNow():
    import Booknow
    Booknow.win.mainloop()


# Explore function:
def explore():
    inibutton.destroy()
    label1.destroy()
    my_label = Label(root, text='Are you going on a trip or a tour?', font=('Georgia', 35), bg='light yellow')
    my_label.place(x=w / 3 - 100, y=290)

    def tour():
        # Update buttons and label
        my_label.config(text='Which mode of transport?')
        button1.config(text='Train', command=train)
        button2.config(text='Plane', command=plane)
        button3 = Button(root, text='Car', font=('Georgia', 20), cursor='hand2', bd=10, command=car)
        button3_window = my_canvas.create_window(w / 4 + 70, h / 2, anchor='center', window=button3)

    # Add button
    button1 = Button(root, text='Trip', font=('Georgia', 20), cursor='hand2', bd=10, command=trip)
    button1_window = my_canvas.create_window(w / 3 + 150, h / 2, anchor='center', window=button1)
    button2 = Button(root, text='Tour', font=('Georgia', 20), cursor='hand2', bd=10, command=tour)
    button2_window = my_canvas.create_window(w / 3 + 350, h / 2, anchor='center', window=button2)
    bookbutton = Button(root, text='Book Now', font=('Georgia', 15, 'bold'), cursor='hand2', bd=10, command=bookNow)
    bookbutton_window = my_canvas.create_window(100, 50, anchor='center', window=bookbutton)
    # Create tooltip
    tip = Balloon(root)
    # Bind tooltip to button
    tip.bind_widget(bookbutton, balloonmsg='Book a ticket to your dream destination')
    tip.subwidget('label').forget()


# Set image in canvas
my_canvas.create_image(0, 0, image=bg1, anchor='nw')

my_canvas.create_text(w / 4, 50, text='WELCOME TO TRAVEL GUIDE', font=('Georgia', 50), fill='white', anchor='nw')
my_canvas.create_text(w / 2, 130, text='Your travel. Your choice.', font=('Georgia', 20), fill='white', anchor='center')
starter = 'This guide comprises of many destinations you may wish to travel to.\nWe hope our guide is ' \
          'helpful.\nIf you want to explore then click "Explore" '
label1 = Label(root, text=starter, font=('Georgia', 20), bg='light yellow')
label1.place(x=w / 3 - 100, y=290)
inibutton = Button(root, text='Explore', font=('Georgia', 15, 'bold'), cursor='hand2', bd=10, command=explore)
inibutton_window = my_canvas.create_window(w / 3 + 300, h / 2, anchor='center', window=inibutton)

root.mainloop()

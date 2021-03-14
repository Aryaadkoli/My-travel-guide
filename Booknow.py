from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# --Creating a tkinter window--
win = Tk()
win.title('Ticket booking')
win.geometry('600x600+400+100')
win.resizable(0, 0)

Label(win, text="Book a ticket here", width=20, font=("bold", 20)).place(x=90, y=53)

# --'StringVar()' :It is used to get the instance of input field--
Fullname = StringVar()
Email = StringVar()

# --Entry space for full name--
Label(win, text="Full Name:", width=20, font=("bold", 10)).place(x=100, y=130)
entry_1 = Entry(win, textvar=Fullname).place(x=240, y=130)

# --Entry space for email id--
Label(win, text="Email id:", width=20, font=("bold", 10)).place(x=90, y=180)
entry_2 = Entry(win, textvar=Email).place(x=240, y=180)


# --Function which runs is train check button is selected--
def mode_train(value):
    Label(win, text=value, fg='white').place(x=0, y=0)
    Label(win, text='From:', width=20, font=("bold", 10)).place(x=90, y=320)
    drop_option_1 = ttk.Combobox(win, state='readonly', justify=CENTER)
    drop_option_1['values'] = ('select', 'Bangalore', 'Hassan')
    drop_option_1.place(x=240, y=320)
    drop_option_1.current(0)
    Label(win, text='To:', width=20, font=("bold", 10)).place(x=90, y=350)
    drop_option_2 = ttk.Combobox(win, state='readonly', justify=CENTER)
    drop_option_2['values'] = ('select', 'Hubli-Madgaon', 'Ratnagiri-Mangalore', 'Kanyakumari', 'Rameshwaram')
    drop_option_2.place(x=240, y=350)
    drop_option_2.current(0)


# --Function which runs if plane checkbutton is selected--
def mode_plane(value):
    Label(win, text=value, fg='white').place(x=0, y=0)
    Label(win, text='From:', width=20, font=("bold", 10)).place(x=90, y=320)
    drop_option_1 = ttk.Combobox(win, state='readonly', justify=CENTER, cursor="hand2")
    drop_option_1['values'] = ('select', 'Bangalore')
    drop_option_1.place(x=240, y=320)
    drop_option_1.current(0)
    Label(win, text='To:', width=20, font=("bold", 10)).place(x=90, y=350)
    drop_option_2 = ttk.Combobox(win, state='readonly', justify='center', cursor="hand2")
    drop_option_2['values'] = (
        'select', 'Ajanta ellora', 'Darjeeling', 'Elephant beach', 'Gir national park', 'Konark temple',
        'Taj mahal')
    drop_option_2.place(x=240, y=350)
    drop_option_2.current(0)


# --Check buttons for selecting train or plane--
Label(win, text="Train or plane:", width=20, font=("bold", 10)).place(x=90, y=230)
r1 = IntVar()
Checkbutton(win, text="Train", padx=5, variable=r1, cursor="hand2", command=lambda: mode_train(r1.get())).place(
    x=235, y=230)
r2 = IntVar()
Checkbutton(win, text="Plane", padx=20, variable=r2, cursor="hand2", command=lambda: mode_plane(r2.get())).place(
    x=290, y=230)


# --Number of people--
Label(win, text="Number of people:", width=20, font=("bold", 10)).place(x=90, y=280)
drop_option = ttk.Combobox(win, state='readonly', justify='center')
drop_option['values'] = ('select', '1', '2', '3', '4', '5', '6', '7', '8')
drop_option.place(x=240, y=280)
drop_option.current(0)


# --Function which runs when submit button is clicked--
def submit():
    if drop_option.get() == 'select':
        messagebox.showerror('Triplore', 'All boxes to be filled')
    else:
        messagebox.showinfo('Travel guide', 'Thank you for booking with us.☺\n'
                                    'Your ticket and payment method will be emailed to you if proper details are '
                                    'filled.')
        win.destroy()


# --Submit button--
Button(win, text='Submit', width=20, bg='brown', fg='white', command=submit).place(x=180, y=380)

win.mainloop()

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("User Login Panel")
window.geometry("300x200+400+300")
window.config(padx=40, pady=50)

registered_username = "admin"
registered_password = "1234"


def succesful_trial():

    username_label.destroy()
    password_label.destroy()
    username.destroy()
    password.destroy()
    enter_button.destroy()

    message_true = Label(window, text="Entered data is correct\nWelcome", font="Arial 15", fg="green")
    message_true.pack()


    new_window = Toplevel(window)
    new_window.title("Welcome")
    new_window.geometry("200x100")
    welcome_message = Label(new_window, text="Welcome to the system!", font="Arial 12")
    welcome_message.pack(pady=20)


def check_trial():
    entered_username = username.get()
    entered_password = password.get()

    if entered_username == registered_username and entered_password == registered_password:
        succesful_trial()
    else:
        messagebox.showerror("Error", "Invalid username or password")


def enter():
    global username, password, username_label, password_label, enter_button
    username_label = Label(window, text="Username")
    username_label.grid(row=0, column=0)
    password_label = Label(window, text="Password")
    password_label.grid(row=1, column=0)

    username = Entry(window)
    username.grid(row=0, column=1)
    password = Entry(window, show="*")
    password.grid(row=1, column=1)

    enter_button = Button(window, text="Enter", width=10, command=check_trial)
    enter_button.grid(row=2, column=1)


enter()
window.mainloop()

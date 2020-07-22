from tkinter import *
from back_end import Database
import landing_page
import create_user_page

database = Database("py_project.db")


class LoginPage:
    def __init__(self, window, content):
        self.show_login(window, content)

    def show_login(self, window, content):

        login_content = Frame(content)
        login_content.grid(row=1, column=1)

        title_label = Label(login_content, text="ProLog", font="Helvetica 16 bold", pady=16)
        title_label.grid(row=0, column=1, columnspan=3)

        username_label = Label(login_content, text="Username")
        username_label.grid(row=1, column=1)
        username = StringVar()
        username_entry = Entry(login_content, textvariable=username)
        username_entry.grid(row=1, column=2)

        password_label = Label(login_content, text="Password")
        password_label.grid(row=2, column=1)
        password = StringVar()
        password_entry = Entry(login_content, textvariable=password)
        password_entry.grid(row=2, column=2)

        login_button = Button(login_content, text="Login", width=12, command=lambda: self.login(window, content, username.get(), password.get(), login_content))
        login_button.grid(row=1, column=3)

        create_user_button = Button(login_content, text="New user", width=12, command=lambda: self.create_user(window, content, login_content))
        create_user_button.grid(row=2, column=3)

    def login(self, window, content, username, password, login_content):
        is_valid = database.check_login(username, password)

        input_warning = Text(login_content, fg="red", width=35, height=1, pady=2, wrap=WORD)
        input_warning.insert(INSERT, "Please check your input for errors")

        if is_valid:
            login_content.grid_forget()
            landing_page.LandingPage(window, content, username)
        else:
            input_warning.grid(row=0, column=1, columnspan=3)

    def create_user(self, window, content, login_content):
        login_content.grid_forget()
        create_user_page.CreateUserPage(window, content)

from tkinter import *
from back_end import Database
import login_page

database = Database("py_project.db")


class CreateUserPage:
    def __init__(self, window, content):
        self.create_user(window, content)

    def create_user(self, window, content):

        create_user_content = Frame(content)
        create_user_content.grid(row=1, column=1)

        title_label = Label(create_user_content, text="Create User", font="Helvetica 16 bold", pady=16)
        title_label.grid(row=0, column=1, columnspan=3)

        name_label = Label(create_user_content, text="Username")
        name_label.grid(row=3, column=1, sticky=W)
        username = StringVar()
        username_entry = Entry(create_user_content, textvariable=username)
        username_entry.grid(row=3, column=2, sticky=W)

        password_label = Label(create_user_content, text="Password")
        password_label.grid(row=4, column=1, sticky=W)
        password = StringVar()
        password_entry = Entry(create_user_content, textvariable=password)
        password_entry.grid(row=4, column=2, sticky=W)

        password2_label = Label(create_user_content, text="Repeat Password")
        password2_label.grid(row=5, column=1, sticky=W)
        password2 = StringVar()
        password2_entry = Entry(create_user_content, textvariable=password2)
        password2_entry.grid(row=5, column=2, sticky=W)

        age_label = Label(create_user_content, text="Age")
        age_label.grid(row=6, column=1, sticky=W)
        user_age = StringVar()
        user_age_entry = Entry(create_user_content, textvariable=user_age)
        user_age_entry.grid(row=6, column=2, sticky=W)

        height_label = Label(create_user_content, text="Height")
        height_label.grid(row=7, column=1, sticky=W)
        user_height = StringVar()
        user_height_entry = Entry(create_user_content, textvariable=user_height)
        user_height_entry.grid(row=7, column=2, sticky=W)

        weight_label = Label(create_user_content, text="Weight")
        weight_label.grid(row=8, column=1, sticky=W)
        user_weight = StringVar()
        user_weight_entry = Entry(create_user_content, textvariable=user_weight)
        user_weight_entry.grid(row=8, column=2, sticky=W)

        add_user_button = Button(create_user_content, text="Add User", width=12, command=lambda: self.add_user(window, content, create_user_content, username.get(), user_age.get(), user_height.get(), user_weight.get(), password.get(), password2.get()))
        add_user_button.grid(row=9, column=1)

        go_back_button = Button(create_user_content, text="Back", width=10, command=lambda: self.go_back(window, content, create_user_content))
        go_back_button.grid(row=10, column=10)

    def go_back(self, window, content, create_user_content):
        create_user_content.grid_forget()
        login_page.LoginPage(window, content)

    def add_user(self, window, content, create_user_content, username, age, height, weight, password, password2):

        username_warning = Text(create_user_content, fg="red", width=35, height=1, pady=2, wrap=WORD)
        input_warning = Text(create_user_content, fg="red", width=35, height=1, pady=2, wrap=WORD)
        input_warning.insert(INSERT, "Please check your input for errors")

        all_users = database.view_users()

        for user in all_users:
            if username == user[1]:
                username_warning.insert(INSERT, "Username is taken")
                username_warning.grid(row=0, column=1, columnspan=3)
                return

        pwcorrect = False
        if password == password2:
            pwcorrect = True

        try:
            age = int(age)
            height = int(height)
            weight = int(weight)
            input_warning.grid_forget()
        except Exception as e:
            input_warning.grid(row=0, column=1, columnspan=3)
            print(e)

        if isinstance(username, str) and len(username) > 3 and age > 12 and height > 100 and weight > 30 and pwcorrect:
            database.create_user(username, age, height, weight, password)
            create_user_content.grid_forget()
            login_page.LoginPage(window, content)
        else:
            input_warning.grid(row=0, column=1, columnspan=3)
from tkinter import *
from back_end import Database
import datetime
import edit_workout_page
import landing_page
import config

database = Database("py_project.db")


class AddWorkoutPage:
    def __init__(self, content, username):
        self.show_add_workout_page(content, username)

    def show_add_workout_page(self, content, username):

        add_workout_content = Frame(content)
        add_workout_content.grid(row=1, column=1)

        new_workout_label = Label(add_workout_content, text="New Workout", font="Helvetica 14 bold", pady=16)
        new_workout_label.grid(row=0, column=1, columnspan=3)

        workout_date_label = Label(add_workout_content, text="Date (YYYY-MM-DD)")
        workout_date_label.grid(row=1, column=1)
        workout_date = StringVar()
        workout_date_entry = Entry(add_workout_content, textvariable=workout_date)
        workout_date_entry.grid(row=1, column=2)

        add_workout_button = Button(add_workout_content, text="Add", width=12, command=lambda: self.add_workout(add_workout_content, content, workout_date.get(), username))
        add_workout_button.grid(row=1, column=3)

        config.current_content = add_workout_content

        go_back_button = Button(add_workout_content, text="Back", width=10, command=lambda: self.go_back(content, add_workout_content, username))
        go_back_button.grid(row=10, column=10)

    def go_back(self, content, add_workout_content, username):
        add_workout_content.grid_forget()
        landing_page.LandingPage(config.global_window, content, username)

    def add_workout(self, add_workout_content, content, date_input, username):

        input_warning = Text(add_workout_content, fg="red", width=35, height=1, pady=2, wrap=WORD)
        input_warning.insert(INSERT, "Please check your input for errors")

        try:
            date_strings = date_input.split("-")
            date_ints = []
            for string in date_strings:
                date_ints.append(int(string))
            date = datetime.datetime(date_ints[0], date_ints[1], date_ints[2])
            date_as_string = date.strftime("%Y-%m-%d")
            input_warning.grid_forget()
        except Exception as e:
            input_warning.grid(row=0, column=1, columnspan=3)
            print(e)
            return
        user_id = database.get_user_id(username)
        workout_id = database.create_workout(date_as_string, user_id)
        self.edit_workout(add_workout_content, content, workout_id, date_as_string, username)

    def edit_workout(self, add_workout_content, content, workout_id, workout_date, username):
        add_workout_content.grid_forget()
        edit_workout_page.EditWorkoutPage(content, workout_id, workout_date, username)

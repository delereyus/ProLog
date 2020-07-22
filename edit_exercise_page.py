from tkinter import *
from back_end import Database
import confirm_sets_page
import edit_workout_page
import config

database = Database("py_project.db")


class EditExercisePage:
    def __init__(self, content, exercise, workout_id, workout_date, username):
        self.show_edit_exercise_page(content, exercise, workout_id, workout_date, username)

    def show_edit_exercise_page(self, content, exercise, workout_id, workout_date, username):

        edit_exercise_content = Frame(content)
        edit_exercise_content.grid(row=1, column=1)

        username_label = Label(edit_exercise_content, text=exercise, font="Helvetica 14 bold", pady=16)
        username_label.grid(row=0, column=1, columnspan=3)

        sets_label = Label(edit_exercise_content, text="Sets")
        sets_label.grid(row=3, column=1, sticky=W)
        sets = StringVar()
        sets_entry = Entry(edit_exercise_content, textvariable=sets)
        sets_entry.grid(row=3, column=2, sticky=W)

        confirm_sets_button = Button(edit_exercise_content, text="OK", width=10, command=lambda: self.confirm_sets(edit_exercise_content, content, int(sets.get()), exercise, workout_id, workout_date, username))
        confirm_sets_button.grid(row=4, column=1)

        config.current_content = edit_exercise_content

        go_back_button = Button(edit_exercise_content, text="Back", width=10, command=lambda: self.go_back(content, edit_exercise_content, username, workout_id, workout_date))
        go_back_button.grid(row=10, column=10)

    def go_back(self, content, edit_exercise_content, username, workout_id, workout_date):
        edit_exercise_content.grid_forget()
        edit_workout_page.EditWorkoutPage(content, workout_id, workout_date, username)

    def confirm_sets(self, edit_exercise_content, content, sets, exercise, workout_id, workout_date, username):
        edit_exercise_content.grid_forget()
        confirm_sets_page.ConfirmSetsPage(content, sets, exercise, workout_id, workout_date, username)

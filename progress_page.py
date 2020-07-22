from tkinter import *
from back_end import Database
import exercise_progress_page
import landing_page
import config

database = Database("py_project.db")


class ProgressPage:
    def __init__(self, content, username):
        self.show_progress_page(content, username)

    def show_progress_page(self, content, username):
        progress_content = Frame(content)
        progress_content.grid(row=1, column=1)

        username_label = Label(progress_content, text="Progress", font="Helvetica 14 bold", pady=16)
        username_label.grid(row=0, column=1, columnspan=3)

        exercise_name = Label(progress_content, text="Exercise")
        exercise_name.grid(row=1, column=1)

        row = 2

        exercise_list = Listbox(progress_content, height=6, width=35)
        exercise_scroll = Scrollbar(progress_content, orient="vertical")
        exercise_list.grid(row=row+1, column=1, rowspan=6, columnspan=2)
        exercise_scroll.grid(row=row+1, column=3, rowspan=6, sticky=W)
        exercise_list.configure(yscrollcommand=exercise_scroll.set)
        exercise_scroll.configure(command=exercise_list.yview)

        available_exercises = database.view_exercises()
        available_exercises.sort()

        for exercise in available_exercises:
            exercise_list.insert(END, exercise[0])

        exercise_list.bind('<<ListboxSelect>>')

        choose_exercise_button = Button(progress_content, text="Show Progress", width=15, command=lambda: self.show_progress(progress_content, content, exercise_list.get(exercise_list.curselection()), username))
        choose_exercise_button.grid(row=row+3, column=3, sticky=E)

        config.current_content = progress_content

        go_back_button = Button(progress_content, text="Back", width=10, command=lambda: self.go_back(content, progress_content, username))
        go_back_button.grid(row=10, column=10)

    def go_back(self, content, progress_content, username):
        progress_content.grid_forget()
        landing_page.LandingPage(config.global_window, content, username)

    def show_progress(self, progress_content, content, exercise, username):
        progress_content.grid_forget()
        exercise_progress_page.ExerciseProgress(content, username, exercise)

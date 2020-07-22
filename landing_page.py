from tkinter import *
import workouts_page
import add_workout_page
import progress_page
import config


class LandingPage:
    def __init__(self, window, content, username):
        self.show_landing_page(window, content, username)

    def show_landing_page(self, window, content, username):
        config.global_window = window

        landing_content = Frame(content)
        landing_content.grid(row=1, column=1)

        config.logged_in = True
        config.current_user = username
        config.check_if_logged_in(window, content, self)
        config.current_content = landing_content

        username_label = Label(landing_content, text=username, font="Helvetica 14 bold", pady=16)
        username_label.grid(row=0, column=1, columnspan=3)

        workouts_button = Button(landing_content, text="Workouts", width=12, height=6, command=lambda: self.show_workouts(landing_content, content, username))
        workouts_button.grid(row=1, column=1)

        add_workout_button = Button(landing_content, text="Add Workout", width=12, height=6, command=lambda: self.add_workout(landing_content, content, username))
        add_workout_button.grid(row=1, column=2)

        progress_button = Button(landing_content, text="Progress", width=12, height=6, command=lambda: self.show_progress(landing_content, content, username))
        progress_button.grid(row=2, column=1)

        config.current_content = landing_content

    def show_progress(self, landing_content, content, username):
        landing_content.grid_forget()
        progress_page.ProgressPage(content, username)

    def show_workouts(self, landing_content, content, username):
        landing_content.grid_forget()
        workouts_page.WorkoutsPage(content, username)

    def add_workout(self, landing_content, content, username):
        landing_content.grid_forget()
        add_workout_page.AddWorkoutPage(content, username)

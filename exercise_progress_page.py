from tkinter import *
from back_end import Database
import config
import progress_page
import progress_details_page

database = Database("py_project.db")


class ExerciseProgress:
    def __init__(self, content, username, exercise):
        self.display_progress(content, username, exercise)

    def display_progress(self, content, username, exercise):
        display_progress_content = Frame(content)
        display_progress_content.grid(row=1, column=1)

        exercise_label = Label(display_progress_content, text=exercise, font="Helvetica 14 bold", pady=16)
        exercise_label.grid(row=0, column=2, columnspan=3)

        exercise_name = Label(display_progress_content, text="Date")
        exercise_name.grid(row=1, column=1)
        exercise_sets = Label(display_progress_content, text="Total Sets")
        exercise_sets.grid(row=1, column=2)
        exercise_reps = Label(display_progress_content, text="Max Weight")
        exercise_reps.grid(row=1, column=3)
        exercise_weight = Label(display_progress_content, text="Reps At Max")
        exercise_weight.grid(row=1, column=4)
        exercise_rest = Label(display_progress_content, text="Avg. Rest")
        exercise_rest.grid(row=1, column=5)

        exercise_data = database.get_exercises_for_user(username, exercise)
        row = 2

        unique_dates = []

        for single_set in exercise_data:
            if single_set[8] not in unique_dates:
                unique_dates.append(single_set[8])

        unique_dates.sort(reverse=True)

        for unique_date in unique_dates:
            date = Text(display_progress_content, height=1, width=15)
            sets = Text(display_progress_content, height=1, width=15)
            weight = Text(display_progress_content, height=1, width=15)
            reps = Text(display_progress_content, height=1, width=15)
            rest = Text(display_progress_content, height=1, width=15)

            number_of_sets = 0
            for full_exercise in exercise_data:
                if full_exercise[8] == unique_date:
                    number_of_sets += 1

            max_weight = 0
            reps_at_max_weight = 0
            for full_exercise in exercise_data:
                if full_exercise[3] > max_weight and full_exercise[8] == unique_date:
                    max_weight = full_exercise[3]
                    reps_at_max_weight = full_exercise[2]

            rest_times = []
            for full_exercise in exercise_data:
                if full_exercise[8] == unique_date:
                    rest_times.append(full_exercise[4])

            rest_total = 0
            for rest_time in rest_times:
                rest_total += rest_time

            average_rest = rest_total / len(rest_times)

            date.insert(INSERT, str(unique_date))
            sets.insert(INSERT, str(number_of_sets))
            weight.insert(INSERT, str(max_weight))
            reps.insert(INSERT, str(reps_at_max_weight))
            rest.insert(INSERT, str(average_rest))

            date.config(state=DISABLED)
            sets.config(state=DISABLED)
            weight.config(state=DISABLED)
            reps.config(state=DISABLED)
            rest.config(state=DISABLED)

            date.grid(row=row, column=1)
            sets.grid(row=row, column=2)
            weight.grid(row=row, column=3)
            reps.grid(row=row, column=4)
            rest.grid(row=row, column=5)

            exercise_details_button = Button(display_progress_content, text="Details", width=10, command=lambda un_date=unique_date: self.show_exercise_details(content, display_progress_content, un_date, exercise_data, username, exercise))
            exercise_details_button.grid(row=row, column=6)

            row += 1
        go_back_button = Button(display_progress_content, text="Back", width=10, command=lambda: self.go_back(content, display_progress_content, username))
        go_back_button.grid(row=10, column=10)

        config.current_content = display_progress_content

    def show_exercise_details(self, content, display_progress_content, un_date, exercise_data, username, exercise):
        display_progress_content.grid_forget()
        progress_details_page.ProgressDetailsPage(content, un_date, exercise_data, username, exercise)

    def go_back(self, content, display_progress_content, username):
        display_progress_content.grid_forget()
        progress_page.ProgressPage(content, username)
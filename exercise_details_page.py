from tkinter import *
from back_end import Database
import edit_workout_page
import config

database = Database("py_project.db")


class ExerciseDetailsPage:
    def __init__(self, content, exercise, workout_id, workout_date, username):
        self.show_exercise_details_page(content, exercise, workout_id, workout_date, username)

    def show_exercise_details_page(self, content, exercise, workout_id, workout_date, username):
        exercise_details_content = Frame(content)
        exercise_details_content.grid(row=1, column=1)

        exercise_label = Label(exercise_details_content, text=workout_date, font="Helvetica 14 bold", pady=16)
        exercise_label.grid(row=0, column=2, columnspan=3)

        exercise_name = Label(exercise_details_content, text="Exercise")
        exercise_name.grid(row=1, column=1)
        exercise_sets = Label(exercise_details_content, text="Set")
        exercise_sets.grid(row=1, column=2)
        exercise_reps = Label(exercise_details_content, text="Reps")
        exercise_reps.grid(row=1, column=3)
        exercise_weight = Label(exercise_details_content, text="Weight")
        exercise_weight.grid(row=1, column=4)
        exercise_rest = Label(exercise_details_content, text="Rest")
        exercise_rest.grid(row=1, column=5)

        row = 2

        all_sets = database.view_exercises_by_workout(workout_id)
        chosen_sets = []

        for single_set in all_sets:
            if single_set[1] == exercise:
                chosen_sets.append(single_set)

        for full_exercise in chosen_sets:
            name = Text(exercise_details_content, height=1, width=15)
            sets = Text(exercise_details_content, height=1, width=15)
            reps = Text(exercise_details_content, height=1, width=15)
            weight = Text(exercise_details_content, height=1, width=15)
            rest = Text(exercise_details_content, height=1, width=15)

            name.insert(INSERT, str(full_exercise[1]))
            sets.insert(INSERT, str(full_exercise[6]))
            reps.insert(INSERT, str(full_exercise[2]))
            weight.insert(INSERT, str(full_exercise[3]))
            rest.insert(INSERT, str(full_exercise[4]))

            name.config(state=DISABLED)
            sets.config(state=DISABLED)
            reps.config(state=DISABLED)
            weight.config(state=DISABLED)
            rest.config(state=DISABLED)

            name.grid(row=row, column=1)
            sets.grid(row=row, column=2)
            reps.grid(row=row, column=3)
            weight.grid(row=row, column=4)
            rest.grid(row=row, column=5)

            row += 1
        go_back_button = Button(exercise_details_content, text="Back", width=10, command=lambda: self.go_back(content, exercise_details_content, workout_id, workout_date, username))
        go_back_button.grid(row=10, column=10)

        config.current_content = exercise_details_content

    def go_back(self, content, exercise_details_content, workout_id, workout_date, username):
        exercise_details_content.grid_forget()
        edit_workout_page.EditWorkoutPage(content, workout_id, workout_date, username)

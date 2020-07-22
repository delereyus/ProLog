from tkinter import *
from back_end import Database
import edit_workout_page
import edit_exercise_page
import config

database = Database("py_project.db")


class ConfirmSetsPage:
    def __init__(self, content, sets, exercise, workout_id, workout_date, username):
        self.show_confirm_sets_page(content, sets, exercise, workout_id, 1, workout_date, username)

    def show_confirm_sets_page(self, content, sets, exercise, workout_id, set_number, workout_date, username):

        edit_sets_content = Frame(content)
        edit_sets_content.grid(row=1, column=1)

        username_label = Label(edit_sets_content, text=exercise, font="Helvetica 14 bold", pady=16)
        username_label.grid(row=0, column=2, columnspan=3)

        weight_label = Label(edit_sets_content, text="Weight")
        weight_label.grid(row=1, column=2)

        reps_label = Label(edit_sets_content, text="Repetitions")
        reps_label.grid(row=1, column=3)

        rest_label = Label(edit_sets_content, text="Rest")
        rest_label.grid(row=1, column=4)

        set_label = Label(edit_sets_content, text="Set " + str(set_number))
        set_label.grid(row=2, column=1)

        weight = StringVar()
        weight_entry = Entry(edit_sets_content, textvariable=weight)
        weight_entry.grid(row=2, column=2, sticky=W)

        reps = StringVar()
        reps_entry = Entry(edit_sets_content, textvariable=reps)
        reps_entry.grid(row=2, column=3, sticky=W)

        rest = StringVar()
        rest_entry = Entry(edit_sets_content, textvariable=rest)
        rest_entry.grid(row=2, column=4, sticky=W)

        add_exercise_button = Button(edit_sets_content, text="Confirm", width=12, command=lambda: self.confirm_exercise(content, edit_sets_content, exercise, workout_id, workout_date, sets, set_number, weight.get(), reps.get(), rest.get(), username))
        add_exercise_button.grid(row=2, column=5, sticky=W)

        config.current_content = edit_sets_content

        go_back_button = Button(edit_sets_content, text="Back", width=10, command=lambda: self.go_back(content, edit_sets_content, username, workout_id, workout_date, exercise))
        go_back_button.grid(row=10, column=10)

    def go_back(self, content, edit_sets_content, username, workout_id, workout_date, exercise):
        config.saved_sets = []
        edit_sets_content.grid_forget()
        edit_exercise_page.EditExercisePage(content, exercise, workout_id, workout_date, username)

    def confirm_exercise(self, content, edit_sets_content, exercise, workout_id, workout_date, sets, set_number, weight, reps, rest, username):

        input_warning = Text(edit_sets_content, fg="red", width=35, height=1, pady=2, wrap=WORD)
        input_warning.insert(INSERT, "Please check your input for errors")

        try:
            weight_as_float = float(weight)
            reps_as_int = int(reps)
            rest_as_int = int(rest)
        except Exception as e:
            input_warning.grid(row=0, column=1, columnspan=3)
            print(e)
            return

        existing_sets = 0
        exercises_this_workout = database.view_exercises_by_workout(workout_id)
        for single_set in exercises_this_workout:
            if single_set[1] == exercise:
                existing_sets += 1

        set_to_save = [exercise, workout_id, weight_as_float, reps_as_int, rest_as_int, set_number + existing_sets]
        config.saved_sets.append(set_to_save)

        if len(config.saved_sets) == sets:
            try:
                for saved_set in config.saved_sets:
                    database.add_exercise(saved_set[0], saved_set[1], saved_set[2], saved_set[3], saved_set[4], saved_set[5])

                config.saved_sets = []
            except Exception as e:
                input_warning.grid(row=set_number+1, column=6)
                print(e)

        edit_sets_content.grid_forget()
        if sets > set_number:
            self.show_confirm_sets_page(content, sets, exercise, workout_id, set_number+1, workout_date, username)
        else:
            edit_workout_page.EditWorkoutPage(content, workout_id, workout_date, username)

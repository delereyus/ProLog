from tkinter import *
from back_end import Database
import edit_exercise_page
import exercise_details_page
import workouts_page
import config

database = Database("py_project.db")


class EditWorkoutPage:
    def __init__(self, content, workout_id, workout_date, username):
        self.show_edit_workout_page(content, workout_id, workout_date, username)

    def show_edit_workout_page(self, content, workout_id, workout_date, username):

        choose_exercise_content = Frame(content)
        choose_exercise_content.grid(row=1, column=1)

        exercise_label = Label(choose_exercise_content, text=workout_date, font="Helvetica 14 bold", pady=16)
        exercise_label.grid(row=0, column=1, columnspan=3)

        exercise_name = Label(choose_exercise_content, text="Exercise")
        exercise_name.grid(row=1, column=1)
        exercise_sets = Label(choose_exercise_content, text="Sets")
        exercise_sets.grid(row=1, column=2)

        row = 2
        workout_id = int(workout_id)

        all_sets = database.view_exercises_by_workout(workout_id)
        unique_exercises = []

        for single_set in all_sets:
            if single_set[1] not in unique_exercises:
                unique_exercises.append(single_set[1])

        for exercise_name in unique_exercises:
            name = Text(choose_exercise_content, height=1, width=15)
            sets = Text(choose_exercise_content, height=1, width=15)

            number_of_sets = 0

            for one_set in all_sets:
                if one_set[1] == exercise_name:
                    number_of_sets += 1

            name.insert(INSERT, str(exercise_name))
            sets.insert(INSERT, str(number_of_sets))

            name.config(state=DISABLED)
            sets.config(state=DISABLED)

            name.grid(row=row, column=1)
            sets.grid(row=row, column=2)
            exercise_details_button = Button(choose_exercise_content, text="Details", width=10, command=lambda ex_name=exercise_name: self.show_exercise_details(content, choose_exercise_content, ex_name, workout_id, workout_date, username))
            exercise_details_button.grid(row=row, column=3)

            row += 1

        exercise_list = Listbox(choose_exercise_content, height=6, width=35)
        exercise_scroll = Scrollbar(choose_exercise_content, orient="vertical")
        exercise_list.grid(row=row+1, column=1, rowspan=6, columnspan=2)
        exercise_scroll.grid(row=row+1, column=3, rowspan=6, sticky=W)
        exercise_list.configure(yscrollcommand=exercise_scroll.set)
        exercise_scroll.configure(command=exercise_list.yview)

        available_exercises = database.view_exercises()
        available_exercises.sort()

        for exercise in available_exercises:
            exercise_list.insert(END, exercise[0])

        exercise_list.bind('<<ListboxSelect>>')

        choose_exercise_button = Button(choose_exercise_content, text="Add", width=10, command=lambda: self.edit_exercise(choose_exercise_content, content, exercise_list.get(exercise_list.curselection()), workout_id, workout_date, username))
        choose_exercise_button.grid(row=row+3, column=3, sticky=E)

        go_back_button = Button(choose_exercise_content, text="Back", width=10, command=lambda: self.go_back(content, choose_exercise_content, username))
        go_back_button.grid(row=10, column=10)

        config.current_content = choose_exercise_content

    def go_back(self, content, choose_exercise_content, username):
        choose_exercise_content.grid_forget()
        workouts_page.WorkoutsPage(content, username)

    def show_exercise_details(self, content, choose_exercise_content, exercise, workout_id, workout_date, username):
        print(exercise)
        choose_exercise_content.grid_forget()
        exercise_details_page.ExerciseDetailsPage(content, exercise, workout_id, workout_date, username)

    def edit_exercise(self, choose_exercise_content, content, exercise, workout_id, workout_date, username):
        choose_exercise_content.grid_forget()
        edit_exercise_page.EditExercisePage(content, exercise, workout_id, workout_date, username)

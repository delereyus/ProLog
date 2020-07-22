from tkinter import *
from back_end import Database
import edit_workout_page
import landing_page
import config

database = Database("py_project.db")


class WorkoutsPage:
    def __init__(self, content, username):
        self.show_workouts(content, username)

    def show_workouts(self, content, username):

        workouts_content = Frame(content)
        workouts_content.grid(row=1, column=1)

        username_label = Label(workouts_content, text=username, font="Helvetica 14 bold", pady=16)
        username_label.grid(row=0, column=1, columnspan=3)

        for usr in database.view_users():
            if usr[1] == username:
                user = usr
                break

        workout_list_label = Label(workouts_content, text="Completed Workouts")
        workout_list_label.grid(row=2, column=1)
        workout_list = Listbox(workouts_content, height=6, width=35)
        workout_scroll = Scrollbar(workouts_content, orient="vertical")
        workout_list.grid(row=3, column=1, rowspan=6, columnspan=2)
        workout_scroll.grid(row=3, column=3, rowspan=6, sticky=W)
        workout_list.configure(yscrollcommand=workout_scroll.set)
        workout_scroll.configure(command=workout_list.yview)

        completed_workouts = database.view_workouts(user[0])
        sorted_workouts = sorted(completed_workouts, key=lambda x: x[1], reverse=True)

        for workout in sorted_workouts:
            workout_list.insert(END, workout[1] + "                                                                      " + '.' + str(workout[0]))

        workout_list.bind('<<ListboxSelect>>')

        choose_workout_button = Button(workouts_content, text="Edit", width=12, command=lambda: self.edit_workout(workouts_content, content, workout_list.get(workout_list.curselection()), username))
        choose_workout_button.grid(row=5, column=4, sticky=W)

        config.current_content = workouts_content

        go_back_button = Button(workouts_content, text="Back", width=10, command=lambda: self.go_back(content, workouts_content, username))
        go_back_button.grid(row=10, column=10)

    def go_back(self, content, workouts_content, username):
        workouts_content.grid_forget()
        landing_page.LandingPage(config.global_window, content, username)

    def edit_workout(self, workouts_content, content, workout_id, username):
        print(workout_id)
        split_string = workout_id.split(".")
        actual_id = split_string[1]
        workout_date = split_string[0]
        date_without_space = workout_date.replace(" ", "")
        print(date_without_space)
        workouts_content.grid_forget()
        edit_workout_page.EditWorkoutPage(content, actual_id, date_without_space, username)

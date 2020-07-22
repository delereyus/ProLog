from tkinter import *
from back_end import Database
import login_page
import landing_page
import config

database = Database("py_project.db")


def startup():
    window = Tk()
    window.geometry("800x600")
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(2, weight=1)
    window.columnconfigure(2, weight=1)
    window.wm_title("ProLog")

    content = Frame(window)
    content.grid(row=1, column=1)

    login_page.LoginPage(window, content)
    window.mainloop()


config.startup()

# back_button = Button(content, width=12, text="Back", command=lambda: go_back(last_window_list[-1]))
# back_button.grid(row=10, column=3)

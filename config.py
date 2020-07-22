from tkinter import *
import login_page

global_window = ''
current_user = ''
current_content = ''
saved_sets = []
logged_in = False


def check_if_logged_in(window, content, landing_page):
    if logged_in:
        menu = Menu(window)
        window.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)

        filemenu.add_command(label="Home", command=lambda: go_home(window, content, landing_page, current_user))
        filemenu.add_separator()
        filemenu.add_command(label="Log Out", command=lambda: logout(window))


def logout(window):
    global logged_in
    logged_in = False
    global saved_sets
    saved_sets = []
    window.destroy()
    startup()


def go_home(window, content, land_page, username):
    if not isinstance(current_content, str):
        current_content.grid_forget()
    global saved_sets
    saved_sets = []
    land_page.show_landing_page(window, content, username)


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


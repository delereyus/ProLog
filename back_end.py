import sqlite3


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

    def view_users(self):
        self.cur.execute("SELECT * FROM users")
        user_names = self.cur.fetchall()
        return user_names

    def view_exercises(self):
        self.cur.execute("SELECT name FROM exercise_names")
        exercises = self.cur.fetchall()
        return exercises

    def view_exercises_by_workout(self, workout_id):
        self.cur.execute("SELECT * FROM exercises WHERE workout_id = ?", [workout_id])
        exercises = self.cur.fetchall()
        return exercises

    def view_workouts(self, user_id):
        self.cur.execute("SELECT id, date FROM workouts WHERE user_id = ?", [user_id])
        workouts = self.cur.fetchall()
        return workouts

    def get_user_id(self, username):
        self.cur.execute("SELECT id FROM users WHERE username=?", [username])
        user_id = self.cur.fetchall()
        return user_id[0][0]

    def create_user(self, username, age, height, weight, password):
        self.cur.execute("INSERT INTO users (username, age, height, weight, password) VALUES (?, ?, ?, ?, ?)", (username, age, height, weight, password))
        self.conn.commit()

    def create_workout(self, date, user):
        self.cur.execute("INSERT INTO workouts (date, user_id) VALUES (?, ?)", (date, user))
        self.conn.commit()
        self.cur.execute("SELECT MAX(id) FROM workouts")
        workout_id = self.cur.fetchall()
        return workout_id[0][0]

    def add_exercise(self, exercise, workout_id, weight, reps, rest_time, set_number):
        self.cur.execute("INSERT INTO exercises (name, reps, weight, rest_time, workout_id, set_number) VALUES (?, ?, ?, ?, ?, ?)", (exercise, reps, weight, rest_time, workout_id, set_number))
        self.conn.commit()

    def check_login(self, username, password):
        self.cur.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        try:
            response = self.cur.fetchall()
            if response[0][0] > 0:
                return True
        except Exception as e:
            print(e)
            return False

    def get_exercises_for_user(self, username, exercise):
        self.cur.execute("SELECT * FROM workouts_with_exercises WHERE username = ? AND name = ?", (username, exercise))
        exercises = self.cur.fetchall()
        return exercises

    def __del__(self):
        self.conn.close()


# self.starting_exercises = ['Push-up', 'Pull-up', 'Squat', 'Deadlift', 'Bench Press', 'Barbell Row', 'Lat Pulldown', 'Overhead Press', 'Leg Press', 'Bicep Curl', 'Tricep Extension']
# self.cur.execute(
#     "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, age INTEGER, height INTEGER, weight INTEGER, password TEXT NOT NULL)"
# )
# self.cur.execute(
#     "CREATE TABLE IF NOT EXISTS workouts (id INTEGER PRIMARY KEY, date TEXT, user_id INTEGER REFERENCES user(id) ON DELETE CASCADE)"
# )
# self.cur.execute(
#     "CREATE TABLE IF NOT EXISTS exercise_names (id INTEGER PRIMARY KEY, name TEXT UNIQUE)"
# )
# self.cur.execute(
#     "CREATE TABLE IF NOT EXISTS exercises (id INTEGER PRIMARY KEY, name TEXT REFERENCES exercise_names(name), reps INTEGER,"
#     " weight DOUBLE, rest_time INTEGER, workout_id INTEGER REFERENCES workout(id) ON DELETE CASCADE)"
# )
# self.conn.commit()
# try:
#     for i in range(len(self.starting_exercises)):
#         self.cur.execute(
#             "INSERT INTO exercise_names (name) VALUES (?)", (self.starting_exercises[i],)
#         )
#     self.conn.commit()
# except Exception as e:
#     print(e)



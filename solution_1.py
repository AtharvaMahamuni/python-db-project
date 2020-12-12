import sqlite3 as lite


# TODO: functionality goes here
class DatabaseManage (object):

    def __init__(self):
        global con
        try:
            con = lite.connect("courses.db")
            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS course(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create DB!")

    # TODO: create data

    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)", data
                )
                return True
        except Exception:
            return False

    # TODO: read data

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "SELECT * FROM course"
                )
            return cur.fetchall()
        except Exception:
            return False

    # TODO: delete data

    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
            return True
        except Exception:
            return False


# TODO: Provide interface to user

def main():
    print("*"*40)
    print("\n \n:: COURSE MANAGEMENT ::\n")
    print("*"*40)

    db = DatabaseManage()

    print("#"*40)
    print("\n ::USER MANUAL:: \n")
    print("#"*40)

    print("\nPress 1. Insert a new course\n")
    print("Press 2. Show all courses\n")
    print("Press 3. Delete a course (Need id of course)\n")
    print("#"*40)
    print("\n")

    choice = input("\nEnter a choice: ")

    if choice == "1":
        name = input("\nEnter course name: ")
        description = input("\nEnter description: ")
        price = input("\nEnter price: ")
        private = input("\nIs this course Private (0/1): ")

        if db.insert_data([name, description, price, private]):
            print("Course wa inserted successfully")
        else:
            print("Oops!!! Something is wrong.")

    elif choice == "2":
        print("\n :: Course List :: \n")

        for index, item in enumerate(db.fetch_data()):
            print("\n")
            print("Course Id:  " + str(item[0]))
            print("Course Name:  " + str(item[1]))
            print("Course Description:  " + str(item[2]))
            print("Course Price:  " + str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print("Is Private: " + private)
            print("\n")

    elif choice == "3":
        record_id = input("\nEnter the course ID: ")

        if db.delete_data(record_id):
            print("\nCourse was successfully deleted")
        else:
            print("\nOops somethint went wrong")

    else:
        print("\nINVALID CHOICE")


if __name__ == "__main__":
    main()

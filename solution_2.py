import sqlite3 as lite


# TODO: Functionality goes here.
class YoutubeDatabaseManager(object):

    def __init__(self):
        global con
        try:
            con = lite.connect("youtube.db")

            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS youtube_videos(id INTEGER PRIMARY KEY, name TEXT, description TEXT, tags TEXT)")
        except Exception:
            print("Unable to create DB")

    # TODO: Create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO youtube_videos(name, description, tags) VALUES (?, ?, ?)", data)
                return True
        except Exception:
            return False

    # TODO: Read data from database
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * from youtube_videos")
                return cur.fetchall()
        except Exception:
            return False

    # TODO: Delete data from database
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                cur.execute("DELETE FROM youtube_videos where id = ?", [id])
                return True
        except Exception:
            return False


# TODO: Provide interface for user.

def main():
    print("*"*40)
    print("\n:: YOUTUBE MANAGEMENT ::")
    print("*"*40)

    db = DatabaseManage()

    print("#"*40)
    print("\n:: USER MANUAL ::\n")
    print("#"*40)

    print("\nPress 1. Add videos")
    print("\nPress 2. Show the videos")
    print("\nPress 3. Delete video")

    print("#"*40)
    print("\n")

    choice = input("Enter a choice no.: ")

    if choice == "1":
        name = input("Enter video name: ")
        description = input("Enter Description: ")
        n = input("Enter no. of tags: ")

        tags[0] = "default"
        for i in range(0, n):
            tags[i] = input("Enter the tag no."+i+": ")

        print("\n")

    elif choice == "2":
        print("\n:: VIDEO LIST ::")

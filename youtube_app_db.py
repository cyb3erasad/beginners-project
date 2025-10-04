import sqlite3

con = sqlite3.connect("youtuber_manager_app")
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )   
''')

def list_all_videos():
     cur.execute("SELECT * FROM videos")
     for row in cur.fetchall():
          print(row)

def add_video(name, time):
     cur.execute("INSERT INTO videos(name, time) VALUES (?, ?)", (name, time))
     con.commit()

def update_video(id, new_name, new_time):
     cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, id))
     con.commit()

def delete_video(id):
     cur.execute("DELETE FROM videos WHERE id = ?", (id,))
     con.commit()


def main():
        while True:
           print("\n=== Youtube Manager | Choose an option ===\n")
           print("1. List all youtube videos")
           print("2. Add a youtube video")
           print("3. Update youtube video details")
           print("4. Delete youtube video details")
           print("5. Exit the app")
           choose = input("Enter your choice: ")

           if choose == '1':
                print("\n")
                print("*" * 70)
                print("\n")
                list_all_videos()
                print("\n")
                print("*" * 70)
           elif choose == '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
           elif choose == '3':
                id = input("Enter video ID to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")  
                update_video(id, name, time)   
           elif choose == '4':
                id = input("Enter video ID to delete: ")
                delete_video(id)   
           elif choose == '5':
                break
           else:
                print("Invalid number, please try again!")     
        con.close()

if __name__ == "__main__":
    main()
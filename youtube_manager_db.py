import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    print('\n')
    print('*' * 70)
    
    if not rows:
        print("Database is empty")
    else:
        for row in rows:
            print(row)

    print("*" * 70)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_videos(videoId, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, videoId))
    conn.commit()

def delete_videos(videoId):
    cursor.execute("DELETE FROM videos where id = ?", (videoId,))
    conn.commit()

def main():

    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the Video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)
        elif choice == '3':
            videoId = input("Enter video ID to update: ")
            name = input("Enter the new Video name: ")
            time = input("Enter the new video time: ")
            update_videos(videoId, name, time)
        elif choice == '4':
            videoId = input("Enter video ID to Delete: ")
            delete_videos(videoId)
        elif choice == '5':
            break
        else:
            print("Invaid choice!")

    conn.close()

if __name__ == "__main__":
    main()
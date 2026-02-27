from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://ytpy:ytpy@cluster0.4jvetgn.mongodb.net/", tlsAllowInvalidCertificates = True)
# Not a good idea to include id and password in code files
# not a good idea tlsAllowInvalidCertificates

db = client["ytmanager"]
video_collection = db["videos"]

# print(video_collection)

def list_videos():
    print('\n')
    print('*' * 70)
    if video_collection.count_documents({}) == 0:
        print("storage is empty")
    else:
        for video in video_collection.find():
            print(f"ID: {video['_id']}, Name: {video['name']} and Time{video['time']}")
    print('*' * 70)

def add_videos(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_videos(id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(id)}, 
        {"$set": {"name": new_name, "time": new_time}})
    
def remove_videos(id):
    video_collection.delete_one({"_id": ObjectId(id)})

def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add all videos")
        print("3. Update all videos")
        print("4. Delete all videos")
        print("5. Exit")
        choice = input("Enter your Choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Add video name: ")
            time = input("Add video time: ")
            add_videos(name, time)
        elif choice == "3":
            id = input("Enter a id to update: ")
            name = input("Enter a new name: ")
            time = input("Enter a new time: ")
            update_videos(id, name, time)
        elif choice == "4":
            id = input("Enter a id to remove: ")
            remove_videos(id)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
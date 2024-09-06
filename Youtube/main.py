
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/youtube-manager' ,  tlsAllowInvalidCertificates=True)
db = client['youtube-manager']
videos_collection = db['videos']


def list_videos():
    try:
        videos = videos_collection.find()
        for video in videos:
            print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
    except Exception as e:
        print(f"Error listing videos: {e}")

def add_video(name, time):
    try:
        videos_collection.insert_one({"name": name, "time": time})
        print("Video added successfully")
    except Exception as e:
        print(f"Error adding video: {e}")

def update_video(video_id, name, time):
    try:
        videos_collection.find_one_and_update({"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}})
        print("Video updated successfully")
    except Exception as e:
        print(f"Error updating video: {e}")

def delete_video(video_id):
    try:
        videos_collection.find_one_and_delete({"_id": ObjectId(video_id)})
        print("Video deleted successfully")
    except Exception as e:
        print(f"Error deleting video: {e}")



def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to update: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
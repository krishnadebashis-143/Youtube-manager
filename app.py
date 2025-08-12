from pymongo import MongoClient
from bson import ObjectId

# Connect to MongoDB
pymongo_client = MongoClient(
    "mongodb+srv://youtubepy:YOUtube123@cluster0.fjjfjpv.mongodb.net/ytmanager",
    tlsAllowInvalidCertificates=True
)
db = pymongo_client["ytmanager"]
videos_collection = db["videos"]

# Add video
def add_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})
    print("Video added successfully!")

# List videos
def list_videos():
    for video in videos_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

# Update video
def updated_video(video_id, name, time):
    try:
        obj_id = ObjectId(video_id)
    except Exception as e:
        print("❌ Invalid ObjectId format:", e)
        return

    print("🔍 Looking for document with _id:", obj_id)

    result = videos_collection.update_one(
        {"_id": obj_id},
        {"$set": {"name": name, "time": time}}
    )

    print(f"Matched: {result.matched_count}, Modified: {result.modified_count}")


# Delete video
def delete_video(video_id):
    result = videos_collection.delete_one({'_id': ObjectId(video_id)})
    print(f"Deleted: {result.deleted_count}")

# Main loop
def main():
    while True:
        print("\nWelcome to the YouTube Video Manager!")
        print("1. Add Video")
        print("2. View Videos")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Please choose an option (1-5): ")

        if choice == "1":
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            add_video(name, time)
        elif choice == "2":
            list_videos()
        elif choice == "3":
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            updated_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            print("Exiting the YouTube Video Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

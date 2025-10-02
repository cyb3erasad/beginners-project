import json

def load_data():
        try:
          with open("youtube.txt", 'r') as file:
             return json.load(file)

        except FileNotFoundError:
            return []
        
def save_data(videos):
   with open('youtube.txt', 'w') as file:
      json.dump(videos, file) 

def list_all_videos(videos):
   print("\n")
   print("*" * 70)
   for index, video in enumerate(videos, start=1):
      print(f"\n{index}. {video['name']} | Duration: {video['time']}")
   print("\n")
   print("*" * 70)   

def add_yt_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)

def update_yt_video(videos):
   list_all_videos(videos)
   index = int(input("Enter the video number you want to update: "))
   if 1 <= index <= len(videos):
      name = input("Enter the new video name: ")
      time = input("Enter the new video time: ")
      videos[index-1] = {'name': name, 'time': time}
      save_data(videos)
   else:
      print("Inavlid number please try again!")       

def delete_yt_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to delete: "))
    if 1<= index <= len(videos):
       del videos[index-1]
       save_data(videos)
    else:
       print("Inavlid number please try again!")
          
def main():
    videos = load_data()
    while True:
        print("\n=== Youtube Manager | Choose an option ===\n")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update youtube video details")
        print("4. Delete youtube video details")
        print("5. Exit the app")
        choose = input("Enter your choice: ")

        match choose:
            case '1':
              list_all_videos(videos)
            case '2':
              add_yt_video(videos)
            case '3':
              update_yt_video(videos)
            case '4':
              delete_yt_video(videos)
            case '5':
              break
            case _:
              print("Invalid choice please try again!")

if __name__ == "__main__":
    main()                             
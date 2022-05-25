from pytube import YouTube
from moviepy.editor import VideoFileClip

print("")
print("Python YouTube Downloader")
print("")

# YouTube URL
url = input("Enter your YouTube URL: ")
youtube = YouTube(url)


if __name__ == "__main__":
    # Print out title
    print("---" * 30)
    print("Title: ",youtube.title)
    print("---" * 30)
    print("")

    # --- Menu ---
    print("1. Video")
    print("2. Only Audio")
    print("")

    option = input("Choose the output (1, 2): ")

    if option == "1":
        source = youtube.streams.get_highest_resolution()
        source.download()
    elif option == "2":
        source = youtube.streams.filter(only_audio=True)
        print(source)
        source.download()
    else:
        print("Wrong format")
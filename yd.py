from pytube import YouTube
from pytube.cli import on_progress
import os


def main():
    video_url = input('Enter YouTube video URL to download: ')

    if os.name == 'nt':
        file_path = os.getcwd() + '\\'
    else:
        file_path = os.getcwd() + '/'

    print("Downloading...Please Wait")
    yt = YouTube(video_url, on_progress_callback=on_progress)

    yt.streams.order_by('resolution').desc()

    yt = yt.streams[0].download(file_path)
    print("Your Video is download in ",file_path)


if __name__ == '__main__':
    main()

#ex_url = 'https://www.youtube.com/watch?v=668nUCeBHyY&ab_channel=AswanthMohan'
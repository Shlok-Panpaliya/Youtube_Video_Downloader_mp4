from pytube import YouTube
import pytube
import os


# def progress_function(stream, chunk, file_handle, bytes_remaining):
#     print(round((1-bytes_remaining/video.filesize)*100, 3), '% done...')


def main():
    video_url = input('Enter YouTube video URL: ')

    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    name = pytube.extract.video_id(video_url)
    print("Downlaod in process...Please wait")
    YouTube(video_url).streams.filter(only_audio=False).first().download(filename=name)
    
    location = path + name + '.mp4'
    
if __name__ == '__main__':
    main()
# YouTube Video Downloader
# Phil Akagu-Jones
# 11/05/2022

from pytube import YouTube

def complete(stream, fileLocation):
    print(f'Your download is ready and can be found at {fileLocation}')
    
def progress(stream, chunk, bytes):
    progressPercent = f'{round(100 - (bytes/stream.filesize* 100), 1)}%'
    print(progressPercent)

link = input("URL of the video you would like to download: ")
chosenVideo = YouTube(link,
                      on_complete_callback = complete,
                      on_progress_callback = progress)

print(f'Title:  {chosenVideo.title}')
print(f'Author: {chosenVideo.author}')

audio = input("Would you just like the audio? (Y/N): ")

if audio == 'Y':
    chosenVideo.streams.get_audio_only().download()
elif audio == 'N':
    chosenVideo.streams.get_highest_resolution().download()
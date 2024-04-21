import os
from pytube import YouTube
from moviepy.editor import *

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    stream.download(output_path=output_path)
    return stream.default_filename

def convert_to_mp3(input_path, output_path):
    video = AudioFileClip(input_path)
    video.write_audiofile(output_path)

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    output_folder = input("Enter the output folder path: ")

    print("Downloading the video...")
    video_filename = download_youtube_video(youtube_url, output_folder)
    print("Video downloaded successfully!")

    print("Converting to MP3...")
    output_filename = video_filename.replace(".mp4", ".mp3")
    input_path = f"{output_folder}/{video_filename}"
    output_path = f"{output_folder}/{output_filename}"
    convert_to_mp3(input_path, output_path)
    print("Conversion completed!")

    print("Removing the MP4 file...")
    os.remove(input_path)
    print("MP4 file removed successfully!")

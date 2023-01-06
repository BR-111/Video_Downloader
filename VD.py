
from pytube import YouTube
import os 
from pathlib import Path

def main_func():
  link = str(input(" Enter Link: "))
  url = YouTube(link)
  print(" Downlaoding ...")
  # Getting Highest Resolution
  video = url.streams.get_highest_resolution()
  path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
  video.download(path_to_download_folder)
  print(" Downloaded!")


if __name__ == "__main__":
  main_func()
  

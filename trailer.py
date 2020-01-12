from __future__ import unicode_literals
import os
from tkinter import *
from tkinter import filedialog
import glob
import urllib.request
from bs4 import BeautifulSoup
import youtube_dl 

def main():
    root = Tk()
    root.withdraw()
    mypath = filedialog.askdirectory()
    for dir in glob.iglob(mypath +'**/*', recursive=True):
        if os.path.isdir(dir):
            for file in glob.iglob(dir+'**/*', recursive=True):
                file_path = str(file).split("/")[-1]
                film = file_path.split("\\")[-1]
                textToSearch = film + " ita"
                query = urllib.parse.quote(textToSearch)
                url = "https://www.youtube.com/results?search_query=" + query
                response = urllib.request.urlopen(url)
                html = response.read()
                soup = BeautifulSoup(html, 'html.parser')
                for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                    video_url ='https://www.youtube.com' + vid['href']
                print(video_url)
                ydl_opts = {
                    'forceformat': '720p'
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
main()

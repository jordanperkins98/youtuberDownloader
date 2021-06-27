import os, sys
from pytube import YouTube

#takes the first argument after the file when calling
link = sys.argv[1]
print(link)
try:
    #change working directory
    os.chdir("/home/jperkins/Downloads")
except OSError:
    print(os.getcwd())
    print("Cant change directory")

#Uses Pytube download() to download file
print("Downloading....")
YouTube(link).streams.filter(progressive=True).first().download()
"""
This file contains code for downloading Facebook videos.
Author: GlobalCreativeApkDev

The code in this file is inspired by the following site.
https://www.geeksforgeeks.org/download-facebook-video-using-python/
"""


# Importing necessary libraries


import youtube_dl
import copy
import os
import sys


# Set the environment variable to a bundle of trusted CA certificates
os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/certs/ca-certificates.crt'


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating function to download YouTube video.


def download_facebook_video(params, url, download_path):
    # type: (dict, str, str) -> None
    ydl: youtube_dl.YoutubeDL = youtube_dl.YoutubeDL(params)

    # Go to the path to download the video to.
    os.chdir(download_path)

    # Download the video
    ydl.download([url])


# Testing
if __name__ == '__main__':
    clear()
    try:
        url: str = input("Please enter the URL of the Facebook video you want to download: ")
        allowed: list = ["1080p(HD)", "720p", "480p(SD)", "360p", "180p"]
        print("Choose video resolution for the downloaded video: ")
        for i in range(len(allowed) + 1):
            if i < len(allowed):
                print(str(i + 1) + ". " + str(allowed[i]))
            else:
                print(str(i + 1) + ". Any available resolution")

        params: dict = {'no_check_certificate': True}  # initial value
        option: str = input("Enter your option: ")
        if option in allowed:
            # Get the integer in 'option'
            number: str = option.split("p")[0]
            params["format"] = "(mp4,webm)[height<=" + str(number) + "]"

        download_facebook_video(params, url, "videos")

    except:
        print("Invalid link!")
        sys.exit(1)


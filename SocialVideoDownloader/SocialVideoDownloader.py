"""
This file contains code for the library "SocialVideoDownloader"
Author(s):
1. GlobalCreativeApkDev
"""


# Importing necessary libraries


import youtube_dl
import copy
import os

import mpmath
from mpmath import mp, mpf

mp.pretty = True


# Creating necessary classes to be used throughout the library.


class SocialVideoDownloader(object):
    """
    This class contains attributes of a social media video downloader.
    """

    def __init__(self, ydl):
        # type: (youtube_dl.YoutubeDL) -> None
        self.ydl: youtube_dl.YoutubeDL = ydl

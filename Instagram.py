import requests
from bs4 import BeautifulSoup
import re

def get_instagram_reels_url(post_url):
    response = requests.get(post_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Temukan tag <video> yang mengandung URL video Reels
        video_tags = soup.find_all('video', attrs={'class': '_ac69'})
        
        if video_tags:
            video_url = video_tags[0]['src']
            return video_url

    return None

def download_instagram_reels(post_url, output_file='reels_instagram.mp4'):
    video_url = get_instagram_reels_url(post_url)

    if video_url:
        response = requests.get(video_url)
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print('Reels telah diunduh ke', output_file)
    else:
        print('Reels tidak ditemukan atau ada masalah dalam mengunduhnya.')

# Contoh penggunaan modul
if __name__ == "__main__":
    post_url = 'https://www.instagram.com/reel/CyIOJ8rvYgi/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=='
    download_instagram_reels(post_url)

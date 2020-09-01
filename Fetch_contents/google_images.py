from bs4 import BeautifulSoup
import requests
import re
import random
import requests
from PIL import Image
from io import BytesIO

def get_images(topic):
    url = f"https://unsplash.com/s/photos/{topic}"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    Images = [x.get('src') for x in soup.find_all('img', alt=True) if "w=1000" in x.get('src')]
    chosen_images = set([random.choice(Images) for x in range(15)])
    images = list(chosen_images)[:3]
    #image1 = images[0]
    #image2 = images[1]
    #image3 = images[2]
    #return (image1, image2, image3)
    return images

if __name__ == '__main__':
    print(get_images('popcorn'))
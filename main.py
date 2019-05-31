import urllib.request
import os, sys
cwd = os.getcwd()

import requests
baseURL = 'https://www.ebay-kleinanzeigen.de'
page = requests.get(baseURL + '/s-sport-camping/c230')

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
links = soup.select('ul.itemlist-separatedbefore li .text-module-begin a')
pages = [baseURL + link.get('href') for link in links]
# print(pages)

for item in pages:
    itemPage = requests.get(item)
    newSoup = BeautifulSoup(itemPage.content, 'html.parser')
    images = newSoup.select('#viewad-lightbox .imagebox-thumbnail img')
    imageURIs = [image.get('data-imgsrc') for image in images]
    count = 0
    if (len(imageURIs) > 0):
        if not os.path.exists(cwd + '/images/'):
            os.mkdir(cwd + '/images/', 755)
    for imageURI in imageURIs:
        count = count+1
        filename = cwd + '/images/' + item.replace("/", "_") + '-' + str(count) + ".jpg"
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(imageURI, filename)
    
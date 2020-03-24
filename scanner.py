from bs4 import BeautifulSoup
import requests
import re
import sys


def scraper(keyword):
    print('starting scraper')
    listing = []
    for i in range(0,4):
        page = i*10
        URL = 'https://www.google.de/search'
        PARAMETERS = {'q': str(keyword), 'start': int(page)}
        #HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'}
        r = requests.get(URL, params=PARAMETERS) #headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        url_tag = soup.findAll('div')
        for info in url_tag:
            test1 = info
            print(test1)
            test = re.search(r"url\?q=(.+?)\&", str(test1))
            print(test)
            if test is not None:
                url = test.group(1)
                listing.append(url)
            else:
                pass

        list = (set(listing))
        print(*list, sep = '\n')


def main():
    keyword = sys.argv[1]
    print('got keyword')
    scraper(keyword=keyword)


main()
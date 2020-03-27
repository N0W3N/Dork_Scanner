from bs4 import BeautifulSoup
import requests
import re
import sys


def scraper(keyword, number):
    listing = []
    for i in range(0, int(number), 1):
        PAGE = i*10
        URL = 'https://www.google.de/search'
        PARAMETERS = {'q': str(keyword), 'start': int(PAGE)}
        #HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'}
        r = requests.get(URL, params=PARAMETERS) #headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        parse_url = soup.findAll('div')
        for junk_url in parse_url:
            test = re.search(r"url\?q=(.+?)\&", str(junk_url))
            if test is not None:
                url = test.group(1)
                listing.append(url)
            else:
                pass

    url_list = (set(listing))
    print(*url_list, sep='\n')
    print(f'Found {len(url_list)} results.')


def main():
    keyword = sys.argv[1]
    number = sys.argv[2]
    print(f'Starting Docking Scanner\n Looking for keyword {keyword} and returning {number} page/s of results.')
    scraper(keyword=keyword, number=number)


main()

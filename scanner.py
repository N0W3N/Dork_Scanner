from bs4 import BeautifulSoup
import requests
import re
import sys
import agents



def scraper(keyword, number, agent):
    listing = []
    for i in range(0, int(number), 1):
        PAGE = i*10
        URL = 'https://www.google.de/search'
        PARAMETERS = {'q': str(keyword), 'start': int(PAGE)}

        #TODO: parsing headers through parameters is sometimes working. Google rejects the requests sometimes <> search results won't show up.
        HEADERS = {'User-Agent': agent}
        r = requests.get(URL, params=PARAMETERS, headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        parse_url = soup.findAll('div')
        #print(r, soup, parse_url)
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
    #TODO: either move the user-agent part or make it more pythonic. Reformating code in main() seems dumb.
    with open('user_agents.txt', 'r') as r:
        agent = agents.get_random_line(r).replace('\n', '')
    print(f'Starting Docking Scanner\n Looking for keyword {keyword} and returning {number} page/s of results.')
    print(f'Using User-Agent {agent} for this run.')
    scraper(keyword=keyword, number=number, agent=agent)


main()

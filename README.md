# Google Dork Scanner

Just a little fun project for dork scanning and scraping google search results based on a string and preferred number of pages.
It runs on a low-level (network) layer and also relying on raw HTTP connections, which makes it even harder to get properly working
compared to high-level working scripts using i.e. selenium or javascript.
Google is able to detect scanners/scrapers like this and ban it, if too many requests have been initiated at a certain time interval,
also if an invalid User-Agent is being used. 
This project is a pretty good way to learn and adapt to those (and more) situations/detection and work your way around it.

#### How does it work?

You can initiated any google search request by `https://www.google.de/search` + `q` + `start`.
While `q` stays for the following keyword, `start` pretty much only means the current page number of the search result site of google.

Since `q` and `start` are working and used as parameters, the request can initiated easily with 3 simple commands.
For the first ten google search results: `https://www.google.de/search` + `Spaghetti` + `0`
Don't be confused about the 0, but google lists its pages multiplied by 10, starting by 0 for the first page, 10 for the second page, 20 for the third page... and so on.

Next step is to retrieve the URLs of all sites of the result page.
In order to manage that, BeautifulSoup creates a soup (which is just a huge string containing the entire html code of the target-url), where the URLs are (hopefully) located.
The URLs in the first page are located in `'a', class_='BVG0Nb'` but can't be directly accessed in the next following pages.
Google somehow obfuscates that part in other pages, because BeautifulSoup can't locate any URLs even if the HTML tags and classes are set correctly.
So it makes more sense to iterate through the `div`-class, which includes all URLs in the html-code.

An example code would be: `<div><div class="ZINbbc xpd O9g5cc uUPGi"><div class="kCrYT"><a href="/url?q=http://www.army.cz/scripts/detail.php%3Fid%3D5762&amp;sa=U&amp;ved=2ahUKEwjaoI7RoLPoAhWTA4gKHb4nBko4ChAWMAl6BAgGEAE&amp;usg=AOvVaw2Fg94cYwm9aGOAf18kncEL"><div class="BNeawe vvjwJb AP7Wnd">Professional Armed Forces | Ministry of Defence &amp; Armed Forces of ...</div><div class="BNeawe UPmit AP7Wnd">www.army.cz › scripts › detail › id=5762</div></a></div><div class="x54gtf"></div><div class="kCrYT"><div><div class="BNeawe s3v9rd AP7Wnd"><div><div><div class="BNeawe s3v9rd AP7Wnd">It is a decisive part of the Czech Armed Forces (CAF), which, according to the Czech Law No. 219/1999 Coll., referred to as the Defence Law, is comprised also  ...</div></div></div></div></div></div></div></div>`

Everthing after ``amp`` is part of Googles own engine and is neither required to access the actual URL nor upcoming usage.  
To remove this chunk from the URL, regular expression (Regex) comes to work and not only looks for patterns like this but also removes and reformat the URL.  
`url\?q=(.+?)\&`  matches the characters `url` literally (case sensitive) and `\?` but with an escape sequence, `q=` literally, puts everything after that `(.+?)` in a group until it hits the breaking point `\&`.

Since regex puts everthing after `?q=` until `\&` in group, this group can be called and used as a variable.

Output of group: http://www.army.cz/scripts/detail.php%3Fid%3D5762`

### Usage

`python3 scanner.py <keyword>`

### Misc.

Code is still in development
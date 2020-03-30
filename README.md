# Google Dork Scanner

Just a little fun project for dork scanning and scraping google search results based on a string and preferred number of pages.
It runs on a low-level (network) layer and also relying on raw HTTP connections, which makes it even harder to get properly working
compared to high-level working scripts using i.e. selenium or javascript.
Google is able to detect scanners/scrapers like this and ban it, if too many requests have been initiated at a certain time interval,
also if an invalid User-Agent is being used. 
This project is a pretty good way to learn and adapt to those (and more) situations/detection and work your way around it.

#### What's a dork scanner anyway?

Dork Scanner are mostly used for scraping web search engines with 'dorks' you provide, in order to find vulnerable urls, web urls or even classified data.
Dorks are some kind of special keywords - such as error messages, parameters or even just normal words, which search engines are able to crawl and index.

Example: `"Index of /password"`  
`"mysql dump" filetype:sql`  
`"Welcome to Administration" "General" "Local Domains" "SMTP Authentication" inurl:admin`

and so on.

Short saying: You're able to find and access sensitive data and information, even if you're not allowed to. Those tools are mainly used by security researchers or hackers.

To retrieve the latest google dork list, I recommend [the latest Google Dork List](https://gbhackers.com/latest-google-dorks-list/).

#### How does it work?

You can initiated any google search request by `https://www.google.de/search` + `q` + `start`.
While `q` stays for the following keyword, `start` pretty much only means the current page number of the search result site of google.

Since `q` and `start` are working and used as parameters, the request can initiated easily with 3 simple commands.
For the first ten google search results: `https://www.google.de/search` + `Fortnite` + `0`
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

Since regex puts everything after `?q=` until `\&` in group, this group can be called and used as a variable.

Output of group: http://www.army.cz/scripts/detail.php%3Fid%3D5762`

### Usage

`python3 scanner.py <keyword> <pages>`

`<keyword>` -> keyword 

`pages` -> number of pages

e.g. `python3 scanner.py Fortnite 3`

Code shall return at least 30 search results

```Starting Docking Scanner
Looking for keyword Fortnite and returning 3 page/s of results.
https://www.facebook.com/FortniteGame/  
https://www.epicgames.com/fortnite/en-US/mobile/android  
https://www.pcgames.de/Fortnite-Spiel-16272/News/Update-bringt-Aurum-Skin-Gratis-Items-Herausforderungen-1346416/  
https://www.giga.de/tipp/fortnite-steamy-stacks-seilrutsche-geheimgang-fundorte/  
https://www.youtube.com/channel/UClG8odDC8TS6Zpqk9CGVQiQ  
https://paninishop.de/games-film/fortnite/  
https://www.rnd.de/themen/fortnite/  
https://www.epicgames.com/fortnite/de/mobile/android/get-started  
https://www.epicgames.com/fortnite/de/download  
https://www.epicgames.com/fortnite/de/chapter2  
https://accounts.google.com/ServiceLogin%3Fcontinue%3Dhttps://www.google.de/search%253Fq%253DFortnite%2526start%253D10%26hl%3Dde  
https://accounts.google.com/ServiceLogin%3Fcontinue%3Dhttps://www.google.de/search%253Fq%253DFortnite%2526start%253D20%26hl%3Dde  
https://www.amazon.de/Deep-Silver-Fortnite-PC/dp/B071GNYTG6  
https://de.wikipedia.org/wiki/Fortnite  
https://www.buffed.de/Fortnite-Spiel-16272/  
https://www.epicgames.com/fortnite/de/news  
https://www.xbox.com/de-DE/games/fortnite  
https://twitter.com/fortnitegame  
https://accounts.google.com/ServiceLogin%3Fcontinue%3Dhttps://www.google.de/search%253Fq%253DFortnite%2526start%253D0%26hl%3Dde  
https://www.youtube.com/watch%3Fv%3Dgb45zVHDxbE  
https://www.kicker.de/1000002052186/video  
https://support.google.com/webmasters/answer/7489871%3Fhl%3Dde  
https://www.pcgames.de/Fortnite-Spiel-16272/News/Details-Patch-Notes-Update-1221-das-steckt-drin-1346266/  
https://epicgames.helpshift.com/a/fortnite/  
https://www.amazon.com/stores/page/92DB4595-1191-4F3E-93AE-C43B20671040  
https://www.playstation.com/de-de/games/fortnite-ps4/  
https://www.ingame.de/guides/fortnite-battle-royale-modus-epic-games-cary-season-event-streamer-koop-survival-twitch-youtube-13593712.html  
https://www.twitch.tv/directory/game/Fortnite  
https://www.epicgames.com/fortnite  
https://www.epicgames.com/fortnite/de/home  
http://fortnitegame.com/  
https://webhelm.de/fortnite-battle-royale/  
https://mein-mmo.de/fortnite/  
https://de.wikipedia.org/wiki/Unreal_Engine_4  
https://www.tz.de/leben/games/videospiele-fortnite-epic-games-battle-royale-update-zielhilfe-betrug-zr-13593935.html  
https://www.youtube.com/watch%3Fv%3DFaiDbdwE0PI  
https://apps.apple.com/de/app/fortnite/id1261357853  
Found 37 results.```

I don't recommend to scrape more than 5 pages, otherwise Google will ban the IP temporarily, making the script unusable.

### Misc.

Code is still in development
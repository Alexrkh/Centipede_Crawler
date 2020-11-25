#!/usr/bin/env python
# -*- coding: utf-8 -*-


print("""
                            .    .
                             )  (
       _ _ _ _ _ _ _ _ _ _ _(.--.)
     {{ { { { { { { { { { { ( '_')
       >>>>>>>>>>>>>>>>>>>>>>>`--'>
_________           __________             _________          _________                       ______            
__  ____/_____________  /___(_)__________________  /____      __  ____/____________ ___      ____  /____________
_  /    _  _ \_  __ \  __/_  /___  __ \  _ \  __  /_  _ \     _  /    __  ___/  __ `/_ | /| / /_  /_  _ \_  ___/
/ /___  /  __/  / / / /_ _  / __  /_/ /  __/ /_/ / /  __/     / /___  _  /   / /_/ /__ |/ |/ /_  / /  __/  /    
\____/  \___//_/ /_/\__/ /_/  _  .___/\___/\__,_/  \___/      \____/  /_/    \__,_/ ____/|__/ /_/  \___//_/     
                              /_/   
                            Centipede Crawler Python3
                    Author: https://github.com/Alexrkh                                                                            
""")

import re
import requests
import urllib.parse as urlparse
import termcolor

target_url = input("Enter Valid Url: ")
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))


def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(termcolor.colored(("URL Found ->" + link), "green"))
            crawl(link)


crawl(target_url)

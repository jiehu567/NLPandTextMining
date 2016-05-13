# Extract URLs

import urllib
from bs4 import BeautifulSoup
import re

url = 'http://www.presidency.ucsb.edu/2016_election_speeches.php?candidate=70&campaign=2016CLINTON&doctype=5000'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

target = open("/Users/hujie/Documents/NLP/Speeches/data/url.txt", 'w')

for tag in tags:
    url = tag.get('href', None)
    if re.match("^../ws.*",url):
        target.write("http://www.presidency.ucsb.edu" + tag.get('href', None)[2:] + "\n")
        
target.close()
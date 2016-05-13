# batch speech extraction
import urllib
from bs4 import BeautifulSoup
import re

url_file = open("data/url.txt")

i = 0
# dp=[]

for url in url_file:
    print i
    i+=1
    html = urllib.urlopen(url).read()
    pid = re.findall(r"\b\d+\b",url)
    soup = BeautifulSoup(html, 'html.parser')

    infile = soup.get_text()

    copy = False

    begin = infile.rfind("The American Presidency ProjectPromote Your Page Too",)
    end = infile.rfind("Citation:",)
    
    # Get date and location
    tags = soup('meta')    
    
#     for tag in tags:
#        dp = tag.get('content', None)
        
    
    infile = str(infile[begin:end-1].encode('utf-8').strip())
    target = open("data/"+str(pid)[2:8]+"_HillaryClinton.txt", 'w')
    target.write(infile)
    target.close()
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
    meta_content = soup.findAll(attrs={"name":"title"}) 
    date = re.findall(r"(?:January|Feburary|March|April|May|June|July|August|September|October|November|December)\s[0-9]+,\s\d{4}", str(meta_content))
    date = str(date)[2:-2]
    location = re.findall(r"\sin\s(.*)\s-\s", str(meta_content))
    location = str(location)[2:-2]   
    
    infile = str(infile[begin:end-1].encode('utf-8').strip())
    target = open("data/"+str(pid)[2:8]+"_HillaryClinton.txt", 'w')
    target.write(infile)
    target.write("\n\n\n")
    target.write(date)
    target.write("\n")
    target.write(location)
    target.close()
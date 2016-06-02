# -*- coding: utf-8 -*-
"""
Created on Thu May 26 01:43:56 2016

@author: hujie
"""
import urllib
import re
from bs4 import BeautifulSoup  # $ pip install beautifulsoup4

url = 'http://www.gamesradar.com/news/games/'
html = urllib.urlopen(url).read()

# get article name
soup = BeautifulSoup(html , 'html.parser')
script = soup.findAll('script')
article_name = re.findall(r'articleName\":\"(.*?)\"',str(script))
# print article_name


# get url
article_url = re.findall(r'articleUrl\":\[\"(.*?)\"\]',str(script))

for add_url in article_url:
    whole_url = url[0:26] + add_url[3:]
    #print whole_url

# get date

article_date = re.findall(r'publishedDate\":\"(.*?)\"',str(script))

#for date in article_date:
    #print date[0:10]


# Use RAKE to extract key words
import six
import rake
import operator
#import io

stoppath = "SmartStoplist.txt"

rake_object = rake.Rake(stoppath)

target = open("news_"+str(article_date[1][0:10])+".txt", 'w')


    

# Write into file
for i in range(len(article_url)):
    target.write("News Title: "+article_name[i])
    target.write("\n")
    target.write("News Date:  "+article_date[i][0:10])
    target.write("\n")
    target.write("News Link:  "+url[0:26] + article_url[i][3:])
    target.write("\n\n")
    
    
    link = article_url[i]
        
    new_link = url[0:26] + link[3:]
    
    html = urllib.urlopen(new_link).read()

    # get article name
    soup = BeautifulSoup(html , 'html.parser')
    
    tags = soup.findAll('textplugin')
    article = re.findall(r'_blank\">(.*?)<\/p>',str(tags))

    # 1. Split text into sentences
    sentenceList = rake.split_sentences(str(article))

    # generate candidate keywords
    stopwordpattern = rake.build_stop_word_regex(stoppath)
    phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
    # print("Phrases:", phraseList)
    # print("---------------------------------------------")

    # calculate individual word scores
    wordscores = rake.calculate_word_scores(phraseList)
    
    # generate candidate keyword scores
    keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
    # print keywordcandidates
    """
    for candidate in keywordcandidates.keys():
        print "Candidate: %s\t\tscore: %s" % (candidate, keywordcandidates.get(candidate))
    """
    
    # sort candidates by score to determine top-scoring keywords
    sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
    totalKeywords = len(sortedKeywords)
    
    # for example, you could just take the top third as the final keywords
    
    for keyword in sortedKeywords[0:int(totalKeywords / 3)]:
         target.write("Keyword: %s\tscore: %s" % (keyword[0], keyword[1]))
         target.write("\n")
    target.write("\n")
        
target.close()


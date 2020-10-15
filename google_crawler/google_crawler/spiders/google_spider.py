import scrapy 
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector

import pandas as pd


class firstSpider(scrapy.Spider): 
  name = "basic" 
  start_urls = [ 
    "https://www.google.com/search?q=journal+dev"
   ]
  def parse(self, response):
    df = pd.DataFrame()
    xlink = LinkExtractor()
    link_list=[]
    link_text=[]
    divs = response.xpath('//div')
    text_list=[]
    for span in divs.xpath('text()'):
      if len(str(span.get()))>100:
        text_list.append(span.get())
    for link in xlink.extract_links(response):
      if len(str(link))>200 or 'Journal'in link.text:
        #print(len(str(link)),link.text,link,"\n")'''
        link_list.append(link)
        link_text.append(link.text)
    for i in range(len(link_text)-len(text_list)):
      text_list.append(" ")
    df['links']=link_list
    df['link_text']=link_text
    df['text_meta'] = text_list
    df.to_csv('output.csv')
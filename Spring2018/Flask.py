# This code uses beautifulsoup to scrape the Campbell's soup website.
# Zachary Rubin, zrubin@rtc.edu
# CNA 336 Spring 2018

from bs4 import BeautifulSoup
import requests

web_soup = "https://www.campbells.com/campbell-soup/our-soups/" # I like soup
r  = requests.get(web_soup)
soup = BeautifulSoup(r.text, 'html.parser')
#print(r.text)
#grid-list-container
soup_name = soup.find_all('p')
#print(soup_name)
soup_names = []
for i in range(3, 12):
    soup_names.append(soup.find_all('p')[i].get_text())
for i in range(0, len(soup_names)):
    soup_names[i] = soup_names[i].replace('\t', '')
    soup_names[i] = soup_names[i].replace('\n', '')
print(soup_names)
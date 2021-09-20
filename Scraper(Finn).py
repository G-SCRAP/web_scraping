# Finn O'Brien
# Web Scraper
# 9/20/2021

# #ctl00_ContentPlaceHolder1_ctl11_divContent > ul


import bs4
import requests
import os

site = "https://evit.com/high_school_career_training/hs"
cntnt = requests.get(site).content
info = bs4.BeautifulSoup(cntnt, "html.parser")
sitesplit = site.split("/")
filename = sitesplit[2].lstrip()
try:
    file = open(f"ScrapedData/{filename}.txt", "r+")
except IOError:
    if not os.path.exists(os.path.dirname("ScrapedData/")):
        os.mkdir("ScrapedData", 0o777)
    file = open(f"ScrapedData/{filename}.txt", "w+")
for x in info.select("#ctl00_ContentPlaceHolder1_ctl11_divContent > ul"):
    file.write(x.getText())
file.close()

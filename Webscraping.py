"""
Gavin Ogren
Monday September, 20th
Webscraping Evit
"""
import requests
import bs4

#Created Variables
res = requests.get('https://evit.com/high_school_career_training/hs')
soup = bs4.BeautifulSoup(res.text, "html.parser")

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

#Opens file and soup finds html elements
with open('Files/Programs.txt', 'w+') as file:
    for elem in soup.select("#ctl00_ContentPlaceHolder1_ctl11_divContent > ul"):
        file.write(elem.getText())

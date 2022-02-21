import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
from pymongo import MongoClient
import pymongo
import json
from bson.json_util import loads, dumps

headers = {
"User-Agent": "My user agent is Python 3.10.1 + BeautifulSoup 4.10 + requests 2.26 based on Windows 10"
}
url = "https://www.scrapethissite.com/pages/forms/"
time.sleep(5)
response=requests.get(url,headers= headers)
time.sleep(5)
print(response.status_code)
soup = BeautifulSoup(response.text,"html.parser")
hockeys_links = soup.select('.pagination li a',limit=24)
soup.prettify()

for hockey_link in hockeys_links:
    time.sleep(5)
    hockey_all_link = urljoin(url,hockey_link.get('href'))
    time.sleep(5)
    response2= requests.get(hockey_all_link,headers= headers)
    print(response2.status_code,"s")
    time.sleep(5)
    soup2=BeautifulSoup(response2.text,"html.parser")
    time.sleep(5)
    hockeys = soup2.find_all("tr", class_="team")
    time.sleep(5)

    for hockey in hockeys:
      hockey= {
      'Team_Name':hockey.find("td",class_="name").text.strip(),
      'Year':hockey.find("td",class_="year").text.strip(),
      'Wins': hockey.find("td",class_="wins").text.strip(),
      'Losses': hockey.find("td",class_="losses").text.strip(),
      'OT_Losses': hockey.find("td",class_="ot-losses").text.strip(),
      'Win_ratio': hockey.find("td",class_="pct").text.strip(),
      'Goals_For_GF': hockey.find("td",class_="gf").text.strip(),
      'Goals_Against_GA' : hockey.find("td",class_="ga").text.strip(),
      'GF_GA_Summary' : hockey.find("td",class_="diff").text.strip()
}

      client = MongoClient('mongodb://localhost:*****/')
      myMDBD = client["Test"]
      collection = myMDBD['test-collection']
      result = dumps(hockey)
      finalresult = loads(result)
      execute = myMDBD.collection.insert_one(finalresult)











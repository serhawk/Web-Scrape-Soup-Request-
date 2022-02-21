
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
import mysql.connector

maysql= mysql.connector.connect(
  host="localhost",
  user="*****",
  password="*****",
  database = "hockeyteams"
)
print("Connected to database")
cursor= maysql.cursor()
cursor.execute("CREATE TABLE hockeyteamsinfo (id INT AUTO_INCREMENT PRIMARY KEY, Team_Name VARCHAR(255),Year VARCHAR(255),Wins VARCHAR(255),Losses VARCHAR(255),OT_Losses VARCHAR(255),Win_ratio VARCHAR(255),Goals_For_GF VARCHAR(255),Goals_Against_GA VARCHAR(255),GF_GA_Summary VARCHAR(255))")
print("Created table")
headers = {
"User-Agent": " My user agent is Python 3.10.1 + BeautifulSoup 4.10 + requests 2.26 based on Windows 10"
}

url = "https://www.scrapethissite.com/pages/forms/"
time.sleep(5)
response=requests.get(url,headers= headers)
time.sleep(5)
print(response.status_code)
soup = BeautifulSoup(response.text,"html.parser")
hockeys_links = soup.select('.pagination li a',limit=24)

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
    insert_sql = "INSERT INTO hockeyteamsinfo(Team_Name,Year,Wins,Losses,OT_Losses,Win_ratio,Goals_For_GF,Goals_Against_GA,GF_GA_Summary) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    time.sleep(5)
    for hockey in hockeys:
      Team_Name= hockey.find("td",class_="name").text.strip().encode("utf-8")
      Year= hockey.find("td",class_="year").text.strip().encode("utf-8")
      Wins= hockey.find("td",class_="wins").text.strip().encode("utf-8")
      Losses= hockey.find("td",class_="losses").text.strip().encode("utf-8")
      OT_Losses= hockey.find("td",class_="ot-losses").text.strip().encode("utf-8")
      Win_ratio= hockey.find("td",class_="pct").text.strip().encode("utf-8")
      Goals_For_GF= hockey.find("td",class_="gf").text.strip().encode("utf-8")
      Goals_Against_GA = hockey.find("td",class_="ga").text.strip().encode("utf-8")
      GF_GA_Summary = hockey.find("td",class_="diff").text.strip().encode("utf-8")
      cursor.execute(insert_sql, (Team_Name,Year,Wins,Losses,OT_Losses, Win_ratio, Goals_For_GF,Goals_Against_GA, GF_GA_Summary))

maysql.commit()
maysql.close()
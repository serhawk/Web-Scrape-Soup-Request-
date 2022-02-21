import requests
from bs4 import BeautifulSoup
import time
import sqlite3

sql = sqlite3.connect('statesinfo.db')
sql.row_factory=sqlite3.Row
sql.isolation_level= None
c= sql.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS countryinfo(name,capital,population,area)''')


headers = {
"User-Agent": "My user agent is Python 3.10.1 + BeautifulSoup 4.10 + requests 2.26"
}
url = "https://www.scrapethissite.com/pages/simple/"
time.sleep(5)
response=requests.get(url,headers= headers)
time.sleep(5)
print(response.status_code)
soup = BeautifulSoup(response.text,"html.parser")
states= soup.find_all("div","country")

insert_sql= "INSERT INTO stateinfo(name,capital,population,area) VALUES(?,?,?,?);"

for state in states:
 name= state.find("h3").text.strip().encode("utf-8")
 capital= state.find("span","country-capital").text.strip().encode("utf-8")
 population= state.find("span","country-population").text.strip().encode("utf-8")
 area=state.find("span","country-area").text.strip().encode("utf-8")
 c.execute(insert_sql, (name,capital,population,area))
sql.commit()
sql.close()
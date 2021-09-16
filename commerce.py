import requests
from bs4 import BeautifulSoup
import pprint
import json
def scrap_data():
    url="https://webscraper.io/test-sites"
    a=requests.get(url)
    soup=BeautifulSoup(a.text,"html.parser")
    div=soup.find("div",class_="container test-sites")
    site=div.find_all("div",class_="col-md-7 pull-right")

    # site=div.find("h2",class_="site-heading")
    # pagination=site.find_all("h2",class_="site-heading")
    list1=[]
    commers=0
    for i in site:
        commers+=1
        commers_site=i.find("h2",class_="site-heading").a.get_text().strip()
        sites=commers_site
        url1=i.find("h2",class_="site-heading").a["href"]
        url2="https://webscraper.io"+(url1)
        url3=url2
        h={"commers":commers,"commers_site":sites,"url1":url3}
        list1.append(h)
        with open("commers_site.json","w")as file:
            json.dump(list1,file,indent=4)
    return list1
scrap_data()

















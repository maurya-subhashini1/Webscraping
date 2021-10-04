import requests
from bs4 import BeautifulSoup
import json
def scrape_movie_details():
    url="https://www.rottentomatoes.com/m/black_panther_2018"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    # print(soup)
    main_div=soup.find("ul",class_="content-meta info")
    # lable=main_div.find_all("ul",class_="content-meta info")
    li=main_div.find_all("li",class_="meta-row clearfix")
    dic1={}
    list1=[]
    for i in  li:
        reating=i.find("div",class_="meta-value").get_text().strip().replace("\n",' ')
        genre=i.find("div",class_="meta-label subtle").get_text()
        dic1.update({genre:reating})
    list1.append(dic1)
    with open("movie_deatailese.json","w")as file:
        json.dump(list1,file,indent=4)
    return dic1
scrape_movie_details()
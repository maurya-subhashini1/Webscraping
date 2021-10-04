import requests
from top_movie1 import sracp_movie
# import requests
from bs4 import BeautifulSoup
import json
movies_detail_list=sracp_movie
def get_movie_list_details(movies):
    list5=[]
    j=0
    while j<len(movies):
        s=movies[j]["url"]
        a=s
        api=requests.get(a)
        soup=BeautifulSoup(api.text,"html.parser")
        main_div=soup.find("ul",class_="content-meta info")
        li=main_div.find_all("li",class_="meta-row clearfix")
        dic1={}
        list1=[]
        for i in  li:
            reating=i.find("div",class_="meta-value").get_text().strip().replace("\n",' ')
            genre=i.find("div",class_="meta-label subtle").get_text()
        list5.append(dic1)
        with open("movie_deatailese.json","w")as file:
            json.dump(list1,file,indent=4)
        return list5
get_movie_list_details(movies_detail_list)


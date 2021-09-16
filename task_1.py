import requests
from bs4 import BeautifulSoup
import json
def scarp_movie():
    url = "https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    trs=tbody.find_all("tr")

    list_1=[]
    posistion=0
    for i in  trs:
        posistion+=1
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        movie=movie_name

        movie_year=i.find("td",class_="titleColumn").span.get_text()[1:5]
        year=int(movie_year)

        movie_rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        rating=float(movie_rating)

        movie_url=i.find("td",class_="titleColumn").a["href"]
        url="https://www.imdb.com/"+ movie_url
       
        h={"posistion":posistion,"Movie name":movie,"year":year,"rating":rating,"url":url}
        list_1.append(h)
        with open("top_movi.json","w")as f:
            json.dump(list_1,f,indent=6)
    return list_1
scarp_movie()


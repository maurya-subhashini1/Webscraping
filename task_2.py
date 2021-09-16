from task_1 import scarp_movie
import pprint
import json
scrape_top_list=scarp_movie()
def group_by_year(movie):
    # list2=[]
    years=[]
    for i in movie:
        if i["year"]not in years:
            years.append(i["year"])
    movie_dic={i:[] for i in years}
    # print(movie_dic)
    for i in movie:
        year=i["year"]
        for (uppdate_year)in movie_dic:
            if (uppdate_year)==year:
                movie_dic[uppdate_year].append(i)
                    # print(movie_dic1)
    with open("year_name.json","w")as file:
            json.dump(movie_dic,file,indent=5)
    return movie_dic
group_by_year(scrape_top_list)

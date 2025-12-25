from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

yc_webpage = response.text
list_of_titles = []

soup = BeautifulSoup(yc_webpage, "html.parser")
title_test = soup.find_all('h3',class_="title")

for title in title_test:
    list_of_titles.append(title.text)

sorted_list = sorted(list_of_titles, key=lambda x:int(re.search(r'\d+', x).group()))
print(sorted_list)
with open("top 100 movies you must watch", 'w', encoding='utf-8') as file:
    for movie in sorted_list:
        file.writelines(f"{movie}\n")

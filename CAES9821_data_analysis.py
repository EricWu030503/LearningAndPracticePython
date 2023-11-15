import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import openpyxl
from scipy import stats

'''
html_text=requests.get("https://www.boxofficemojo.com/franchise/?ref_=bo_nb_fr_secondarytab").text
soup=BeautifulSoup(html_text,'lxml')
franchises=soup.find_all('td',class_='a-text-left mojo-header-column mojo-truncate mojo-field-type-franchise')
franchise_urls = []
for franchise in franchises:
    franchise_urls.append(franchise.find('a',class_='a-link-normal')["href"])
movie_names = []
for url in franchise_urls:
    text = requests.get("https://www.boxofficemojo.com"+url).text
    mysoup = BeautifulSoup(text, 'lxml')
    movies = mysoup.find_all('td',class_ = 'a-text-left mojo-field-type-release mojo-cell-wide')
    for movie in movies:
        movie_name = movie.find('a',class_='a-link-normal').text
        movie_names.append(movie_name)
movie_names = set(movie_names)
movie_names = list(movie_names)

df_xlsx=pd.read_excel('/Users/owen/Documents/HKU Course Materials/yr2 sem2/CAES9821/Case Study Report Data File 2022-23 S2 FINAL.xlsx')
book= openpyxl.load_workbook('/Users/owen/Documents/HKU Course Materials/yr2 sem2/CAES9821/Case Study Report Data File 2022-23 S2 FINAL.xlsx')
sheet = book.active
excel_movie_names = list(df_xlsx["Movie"])
for i in range(len(excel_movie_names)):
    if excel_movie_names[i] in movie_names:
        sheet.cell(row=2+i,column = 7).value = 1
book.save("CAES9821 Data.xlsx")
'''
df_xlsx=pd.read_excel('/Users/owen/Documents/HKU Course Materials/yr2 sem2/CAES9821/CAES9821 Data.xlsx')
world_gross = list(df_xlsx["WorldWide Gross "])
budget = list(df_xlsx["Production Budget "])
franchise = list(df_xlsx["Franchise"])
world_profit = list(df_xlsx["worldwide profits"])
economic_condition = list(df_xlsx["Economic Condition"])
critic_score=list(df_xlsx["Critic Score (Rotten Tomatoes)"])
r = np.corrcoef(franchise, world_profit)[0][1]
print(stats.pointbiserialr(critic_score, franchise))
plot.scatter(economic_condition,world_profit)

print(r)








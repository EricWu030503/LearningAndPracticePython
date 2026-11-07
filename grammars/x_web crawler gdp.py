from bs4 import BeautifulSoup
import requests
class GDP:
    def __init__(self,year,gdp_growth):
        self.year=year
        self.gdp_growth=gdp_growth
class dj:
    def __init__(self,year,annual_change,open,close):
        self.year=year
        self.annual_change=annual_change
        self.open=open
        self.close=close
html_text=requests.get("https://www.macrotrends.net/countries/USA/united-states/gdp-growth-rate").text
html_text2=requests.get("https://www.macrotrends.net/1319/dow-jones-100-year-historical-chart").text
soup=BeautifulSoup(html_text,'lxml')
soup2=BeautifulSoup(html_text2,'lxml')
years2_data=soup2.find_all('td',style='text-align:center')
up_data=soup2.find_all('td',style='text-align:center; color:green')
down_data=soup2.find_all('td',style="text-align:center; color:red")
other_data=soup2.find_all('td',style='text-align:center;')
other=[]
for a in other_data:
    other.append(a.text)
open=[]
close=[]
increase=[]
decrease=[]
for i in range(1,len(other),5):
    open.append(other[i])
for i in range(4,len(other),5):
    close.append(other[i])
for a in up_data:
    increase.append(a.text)
for a in down_data:
    decrease.append(a.text)
years2=[]
for a in years2_data:
    years2.append(a.text)
years_data=soup.find_all('td',style="text-align:center")
GDP_data=soup.find_all('td',style="text-align:center;")
years=[]
data_set=[]
GDP_growth_rates=[]
for year in years_data:
    years.append(year.text)
for gdp in GDP_data:
    data_set.append(gdp.text)
for i in range(0,len(data_set),2):
    GDP_growth_rates.append(data_set[i])
i=0
gdp_data=[]
while i<len(years):
    data=GDP(years[i],GDP_growth_rates[i])
    gdp_data.append(data)
    i+=1
dj_data=[]
x=1
up_count=1
down_count=0
while x<len(years2):
    if float(open[x].replace(",",''))<float(close[x].replace(",",'')):
        myobject=dj(years2[x],increase[up_count],open[x],close[x])
        up_count+=1
    else:
        myobject=dj(years2[x],decrease[down_count],open[x],close[x])
        down_count+=1
    x+=1
    dj_data.append(myobject)

a=0
while a<len(gdp_data):
    ratio=float(gdp_data[a].gdp_growth.replace("%",''))/float(dj_data[a].annual_change.replace("%",''))
    #print(f"{float(dj_data[a].annual_change.replace('%',''))}      {float(gdp_data[a].gdp_growth.replace('%',''))}")
    if ratio<0.1:
        print(f"year: {gdp_data[a].year}")
        print(f"ratio: {ratio}")
        print("")
    a+=1

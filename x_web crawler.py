from bs4 import BeautifulSoup
import requests
import time
unfamiliar_skills=input("Put some skills that you are not familiar with:")
def find_jobs():
    html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    #print(html_text)
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')#only for the first page of the website
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(" ","")
            skills=job.find('span',class_='srp-skills').text.replace(" ","")
            more_info=job.header.h2.a["href"]
            if unfamiliar_skills not in skills:
                print(f"Company name: {company_name.strip()}")
                print(f"Required skill: {skills.strip()}")
                print(f"More info: {more_info}")
                print('')

if __name__=='__main__':
    while True:
        find_jobs()
        waiting_time=10
        print(f"Please wait for {waiting_time} seconds")
        time.sleep(waiting_time)
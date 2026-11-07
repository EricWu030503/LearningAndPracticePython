from bs4 import BeautifulSoup

with open("/Users/owen/Downloads/HTML/index.html","r") as html_file:
    content=html_file.read()
    #print(content)

    soup=BeautifulSoup(content,"lxml")
    #print(soup.prettify())
    #tags=soup.find('h1')
    tags=soup.find_all("h2")
    #print(tags)
    for tag in tags:
        print(tag.text)
    '''
    course_cards=soup.find_all('div',class_="card")
    for course in course_cards:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
    '''
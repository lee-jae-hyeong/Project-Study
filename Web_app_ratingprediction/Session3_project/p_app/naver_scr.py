import requests
from bs4 import BeautifulSoup

def movie(name) :
    url = f"https://movie.naver.com/movie/search/result.nhn?query={name}&section=all&ie=utf8"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    return int(soup.find('p', class_='result_thumb').find('a').get('href').split('=')[1])

def code(code):
    url = f"https://movie.naver.com/movie/bi/mi/basic.nhn?code={code}"
    page1 = requests.get(url)
    soup = BeautifulSoup(page1.content, 'html.parser')
    genre = soup.find('dl', class_='info_spec').text.replace(', \r','').split('\n')[5]
    genre1 = soup.find('dl', class_='info_spec').text.replace(', \r','').split('\n')[6]
    genre2 = soup.find('dl', class_='info_spec').text.replace(', \r','').split('\n')[7]
    country = soup.find('dl', class_='info_spec').text.replace(', \r','').replace('\r','').split('\n')[8]

    return genre, country, genre1, genre2

def people(name):
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=영화+{name}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    director = soup.find_all('strong', class_='name type_ell_2 _html_ellipsis')[0].text
    actor1 = soup.find_all('strong', class_='name type_ell_2 _html_ellipsis')[1].text
    actor2 = soup.find_all('strong', class_='name type_ell_2 _html_ellipsis')[2].text
    title = soup.find_all('strong', class_='_text')[0].text

    return director, actor1, actor2, title
    

        


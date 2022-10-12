from requests import get
from bs4 import BeautifulSoup
import os
import re

def get_blog_articles():
    url = 'https://codeup.com/blog/'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []
    regexp = r'(http.+)"'

    for link in soup.find_all('h2')[0:6]:
        blog_url = re.findall(regexp, str(link))[0]
        response2 = get(blog_url, headers=headers)
        soup2 = BeautifulSoup(response2.content, 'html.parser')
        content = soup2.find('div', id='main-content').text
        articles.append({'title' : soup2.title.string, 'content' : content})
    return articles


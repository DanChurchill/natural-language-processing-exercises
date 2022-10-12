from requests import get
from bs4 import BeautifulSoup
import os
import re
import pandas as pd

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
        content = soup2.find('div', id='main-content').text.strip()
        articles.append({'title' : soup2.title.string, 'content' : content})
    return pd.DataFrame(articles)

def get_news_articles():
    articles = []

    home_url = 'https://inshorts.com/en/read/'
    cat_list = ['technology', 'sports', 'technology', 'entertainment']
    for cat in cat_list:
        response = get(home_url+cat)
        soup = BeautifulSoup(response.content, 'html.parser')    
        titles = soup.select('div.news-card-title.news-right-box')
        contents = soup.select('div.news-card-content.news-right-box')

        regexp = r'(.+?)\n\n'
        for i in range(len(titles)):
            content = re.findall(regexp, contents[i].text.strip())
            title = re.findall(regexp, titles[i].text.strip())
            articles.append({'title' : title[0], 'content' : content[0], 'category' : cat})
    return pd.DataFrame(articles)



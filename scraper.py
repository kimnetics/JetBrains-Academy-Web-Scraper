import os
import string

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.nature.com'


def get_article_list(list_url, article_type):
    article_list = []

    # Get article list page.
    url = BASE_URL + list_url
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if response.status_code != 200:
        raise Exception(f'Article list at {url} returned {response.status_code}.')

    # Loop through news articles.
    soup = BeautifulSoup(response.content, 'html.parser')
    article_spans = soup.find_all('span', {'class': 'c-meta__type'}, string=article_type)
    for article_span in article_spans:
        article = article_span.find_parent('article')
        article_list.append({
            'description': article.a.text,
            'url': article.a.get('href')
        })

    return article_list


def save_article_to_file(article_url, file_name):
    # Get article page.
    url = BASE_URL + article_url
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if response.status_code != 200:
        raise Exception(f'Article at {url} returned {response.status_code}.')

    # Write page contents to file.
    soup = BeautifulSoup(response.content, 'html.parser')
    with open(file_name, 'wb') as file:
        body_text = soup.find('p', {'class': 'article__teaser'})
        if body_text:
            file.write(bytes(body_text.text.strip(), 'utf-8'))


def main():
    max_page_number = int(input())
    article_type = input()

    # Loop through article list pages.
    for page_number in range(1, max_page_number + 1):
        article_list = get_article_list(f'/nature/articles?sort=PubDate&year=2020&page={page_number}',
                                        article_type)

        # Create output directory if it does not exist.
        directory = f'./Page_{page_number}'
        if os.path.exists(directory):
            if not os.path.isdir(directory):
                raise Exception(f'{directory} is a file not a directory.')
        else:
            os.mkdir(directory)

        # Loop through articles.
        for article in article_list:
            file_name = article['description'].strip()
            file_name = file_name.translate(str.maketrans(' ', '_', string.punctuation))
            save_article_to_file(article['url'], f'{directory}/{file_name}.txt')

        print('Saved all articles.')


main()

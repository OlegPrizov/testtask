from bs4 import BeautifulSoup
import requests

def main_func(url, name):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Ошибка запроса {url}: статус {response.status_code}")
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/'):
            link['href'] = f"/{name}{href}"
    modified_html = str(soup)
    return modified_html

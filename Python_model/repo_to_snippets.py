from bs4 import BeautifulSoup
import requests


def find_python_files(repo_url, crawled=[], python_files=[]):
    html = requests.get(repo_url)
    plain_text = html.text
    crawled.append(repo_url)
    soup = BeautifulSoup(plain_text, 'html.parser')
    elements = soup.find_all('div', class_="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item")
    for element in elements:
        if element.svg.get('aria-label') == 'Directory':
            link = element.a.get('href')
            if link not in crawled:
                print(link)
                find_python_files("https://github.com" + link, crawled=crawled)
        elif element.svg.get('aria-label') == 'File':
            file_name = element.a.get('href')
            if file_name[-2:] == 'py':
                python_files.append("https://github.com" + file_name)

    return python_files


def get_python_code(repo_url):
    code_snippets = []
    for i in find_python_files(repo_url):
        html = requests.get(i)
        plain_text = html.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        raw_button = soup.find('div', class_='d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between')
        url = 'https://github.com'+raw_button.a.get('href')
        print(url)
        html = requests.get(url)
        plain_text = html.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        code_snippets.append(soup.find_all(text=True)[0])
    return code_snippets

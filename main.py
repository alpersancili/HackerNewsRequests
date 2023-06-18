import requests
from bs4 import BeautifulSoup

target_url = "https://news.ycombinator.com/"

def make_request(url):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def find_titles(url):
    links = make_request(url)
    for link in links.find_all("a", rel="noreferrer"):
        print("Title : " + link.string)

find_titles(target_url)


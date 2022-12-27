import requests
from bs4 import BeautifulSoup


ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
     "AppleWebKit/537.36 (KHTML, like Gecko)" \
     "Chrome/108.0.0.0 Safari/537.36"


def get_soup(url):
    response = requests.get(url, headers={"User-Agent": ua})
    return BeautifulSoup(response.content, "html.parser")


url = "https://tokubai.co.jp/"

from parsel import Selector
import time
import requests


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            return response.text

        return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls_novidades = selector.css("div.cs-overlay a::attr(href)").getall()
    return urls_novidades


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    url_next_page_link = selector.css("div.nav-links a.next::attr(href)").get()
    return url_next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

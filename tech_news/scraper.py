import re
from parsel import Selector
import time
import requests
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

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
    noticia = dict()
    selector = Selector(text=html_content)
    noticia["url"] = selector.css("[rel='canonical']::attr(href)").get()
    noticia["title"] = selector.css("h1.entry-title::text").get()
    noticia["timestamp"] = selector.css("li.meta-date::text").get()
    noticia["writer"] = selector.css("span.author a::text").get()
    noticia["comments_count"] = len(selector.css("ol.comment-list").getall())
    paragraph = selector.css("div.entry-content p").get()
    # a linha de código abaixo foi feito com o auxílio
    # da resolução do problema encontrado em
    # source(https://pt.stackoverflow.com/questions/192176/como-remover-tags-em-um-texto-em-python)
    text = re.sub("<[^>]+?>", "", paragraph)
    noticia["summary"] = text.replace("&amp;", "&")
    noticia["tags"] = selector.css("[rel='tag']::text").getall()
    noticia["category"] = selector.css("span.label::text").get()
    return noticia


# Requisito 5
def get_tech_news(amount):
    blog_page = fetch("https://blog.betrybe.com")

    link_news = scrape_novidades(blog_page)

    while len(link_news) < amount:
        next_page = scrape_next_page_link(blog_page)

        blog_page = fetch(next_page)

        page_news_list = scrape_novidades(blog_page)
        link_news.extend(page_news_list)

    news_list = [scrape_noticia(fetch(link)) for link in link_news[:amount]]

    create_news(news_list)

    return news_list

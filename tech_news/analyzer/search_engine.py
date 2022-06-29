from tech_news.database import search_news
from tech_news.utils import date_written_in_full
from datetime import datetime


# Requisito 6
def search_by_title(title):
    print("cheguei aqui 1")
    news_by_title = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}}
    )
    return [(news["title"], news["url"]) for news in news_by_title]


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date)

        news_by_date = search_news(
            {"timestamp": {"$regex": date_written_in_full(date)}}
        )
        return [(news["title"], news["url"]) for news in news_by_date]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

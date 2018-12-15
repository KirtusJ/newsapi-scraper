# Event-Logger-newsapi
A Python client for the [News API](https://newsapi.org/docs/)

Built for development of [Event Logger](https://github.com/KirtusJ/Event-Logger)

# pip install newsapi-scraper

from scrapenewsapi import News

news = News(api_key=api_key)

news.query_top(query="trump", language="en", country="us")

Returns a JSON Object

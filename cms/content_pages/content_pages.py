from config.settings import ROOT, HOME
from utils.soup import *

def home_page(article):
    """
    Returns home page soup with current latest article included
    """ 
    home_html = get_soup(f"{ROOT}/{HOME}")
    latest = selector(home_html, "div.article")
    wipe_content(latest)
    build_article(home_html, latest, article)
    return home_html

def index_page(articles, index_page):
    """
    Returns an index page with all relevant articles included
    """
    index_html = get_soup(index_page)
    article_div = selector(index_html, "main")

    for article in articles:
        build_article(index_html, article_div, article)

    return index_html

def build_article(soup, article_div, article):
    """
    Returns a div.article for a given article
    """
    header = build_elem(soup, "h3")
    inner_text(header, article['title'])
    append_child(article_div, header)

    date = build_elem(soup, "date", datetime=article['date_attr'])
    inner_text(date, article['html_date'].text)
    append_child(article_div, date)

    topic_container = build_elem(soup, "ul")
    class_list(topic_container, "topic-container")
    for keyword in article['keywords']:
        topic = build_elem(soup, "li")
        inner_text(topic, keyword)
        class_list(topic, "topic")
        append_child(topic_container, topic)
    append_child(article_div, topic_container)

    link = f"/{article['directory']}/{article['filename'].replace('.html','')}"
    anchor = build_elem(soup, "a", href=link)
    inner_text(anchor, "Go to article")
    append_child(article_div, anchor)

    desc = build_elem(soup, "p")
    inner_text(desc, article['description'])
    class_list(desc, "description")
    append_child(article_div, desc)

    return article_div

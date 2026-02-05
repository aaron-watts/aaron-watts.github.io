from config.settings import ROOT, HOME, SELECTORS
from utils.soup import *

def home_page(article):
    """
    Returns home page soup with current latest article included
    """ 
    print(f"{ROOT}/{HOME}")
    home_html = get_soup(f"{ROOT}/{HOME}")
    latest = selector(home_html, "article")
    wipe_content(latest)
    build_article(home_html, latest, article)
    return home_html

def index_page(articles, index_page):
    """
    Returns an index page with all relevant articles included
    """
    index_html = get_soup(index_page)
    main_elem = selector(index_html, SELECTORS["index"])
    wipe_content(main_elem)

    for article in articles:
        #build_article(index_html, article_div, article)
        article_div = build_elem(index_html, "article")
        build_article(index_html, article_div, article)
        append_child(main_elem, article_div)

    return index_html

def build_article(soup, article_div, article):
    """
    Returns a div.article for a given article
    """
    header = build_elem(soup, "header")
    h_three = build_elem(soup, "h3")
    inner_text(h_three, article['title'])
    append_child(header, h_three)

    time_elem = build_elem(soup, "time", datetime=article['date_attr'])
    inner_text(time_elem, article['html_date'].text)
    append_child(header, time_elem)

    topic_container = build_elem(soup, "ul")
    class_list(topic_container, "topic-container")
    for keyword in article['keywords']:
        topic = build_elem(soup, "li")
        inner_text(topic, keyword)
        class_list(topic, "topic")
        append_child(topic_container, topic)
    append_child(header, topic_container)

    append_child(article_div, header)

    desc = build_elem(soup, "p")
    inner_text(desc, article['description'])
    class_list(desc, "description")
    append_child(article_div, desc)

    link = f"/{article['directory']}/{article['filename'].replace('.html','')}"
    anchor = build_elem(soup, "a", href=link)
    inner_text(anchor, "Read More")
    append_child(article_div, anchor)

    return article_div

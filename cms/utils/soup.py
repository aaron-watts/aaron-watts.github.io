from datetime import date
from config.settings import BASE_URL, SELECTORS
from bs4 import BeautifulSoup


def wipe_content(parent):
    parent.clear()
    return parent()


def get_soup(f):
    with open(f) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, "lxml")
    return soup

def build_elem(soup, tag, **attrs):
    if attrs:
        elem = soup.new_tag(tag, **attrs)
    else:
        elem = soup.new_tag(tag)
    return elem

def class_list(elem, classlist):
    elem['class'] = classlist
    return elem

def inner_text(elem, text):
    elem.string = text
    return elem

def append_child(parent, child):
    parent.append(child)
    return parent

def selector(soup, selector, attr=None):
    """
    Returns an element from soup,
    if an attribute is provide then returns the value
    """
    if attr:
        return soup.select_one(selector)[attr]
    return soup.select_one(selector)


def format_content(content):
    """
    Formats and returns html to preserve new lines in pre elements
    """
    text = ''
    for child in content.children:
        if not child.name == "section":
            if child.name == "pre":
                text += str(child)
            else:
                text += " ".join(str(child).split())
        else:
            for descendant in child.children:
                if descendant.name == "pre":
                    text += str(descendant)
                else:
                    text += " ".join(str(child).split())
    return text


def extract_data(doc):
    """
    Extracts and returns key data from soup
    """
    keywords = doc['soup'].select_one(SELECTORS['keywords'])['content'].split(",")
    doc['title'] = doc['soup'].select_one(SELECTORS['title']).text
    doc['intro'] = doc['soup'].select_one(SELECTORS['intro']).text
    doc['description'] = " ".join(doc['intro'].split())
    doc['html_date'] = doc['soup'].select_one(SELECTORS['time'])
    doc['date_attr'] = doc['html_date']['datetime']
    doc['date'] = date.fromisoformat(doc['html_date']['datetime'])
    doc['pub_date'] = doc['date'].strftime("%a, %d %b %Y")
    doc['pub_date'] += " 08:00:00 GMT"
    doc['main'] = doc['soup'].select_one(SELECTORS['main'])
    doc['content'] = format_content(doc['main'])
    doc['keywords'] = [kw.lstrip() for kw in keywords]
    return doc

def absolute_urls(html):
    """
    Returns HTML with relative paths replaced by absolute paths
    """
    nl = '\\n'
    rurl = '="/'
    aurl = f'="{BASE_URL}/'
    return str(html).strip().replace(nl, '').replace(rurl, aurl)

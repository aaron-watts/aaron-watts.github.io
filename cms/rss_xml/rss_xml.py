from config.settings import BASE_URL, RSS, FEEDS, NAMESPACES
from utils import xtree
from utils.files import path_to_url, image_url_from_file
from utils.soup import selector, absolute_urls

def build_rss(doc_tree, feed):
    """
    Return RSS XML as tree object
    """
    rss = build_root(feed)
    channel = rss[0]
    if len(doc_tree) > RSS['count']:
        for i in range(RSS['count']):
            build_item(channel, doc_tree[i])
    else:
        for doc in doc_tree:
            build_item(channel, doc)

    return rss


def build_root(feed):
    """
    Return the roots element of an RSS XML document
    """
    # TITLE can be formed from existing data?
    # DESC should come from html description if not All
    ATOM_LINK_HREF = feed['href']
    TITLE = feed['title']
    LINK = feed['link']
    DESC = feed['description']

    rss = xtree.root_element(NAMESPACES['rss'], "rss")
    rss = xtree.set_attribute(rss, "version", "2.0")
    channel = xtree.child_element(rss, "channel")

    atom_link = xtree.child_element(channel, "atom:link")
    xtree.set_attribute(atom_link, "href", ATOM_LINK_HREF)
    xtree.set_attribute(atom_link, "rel", "self")
    xtree.set_attribute(atom_link, "type", "applications/rss+xml")

    xtree.child_element(channel, "title", TITLE)
    xtree.child_element(channel, "link", LINK)
    xtree.child_element(channel, "description", DESC)
    xtree.child_element(channel, "category", "Technology")

    return rss


def build_item(parent, doc):
    """
    Builds XML item for an article
    """
    URL = path_to_url(f"{doc['directory']}/{doc['filename']}")
    IMG = BASE_URL + selector(doc['soup'], "article img", "src")

    item = xtree.child_element(parent, "item")

    xtree.child_element(item, "title", doc['title'])
    xtree.child_element(item, "link", URL)
    xtree.child_element(item, "pubDate", doc['pub_date'])
    xtree.child_element(item, "description", doc['description'])
    xtree.child_element(item, "guid", URL)
    content = absolute_urls(doc['content'])
    xtree.child_element(item, "content:encoded", content)

    enclosure = xtree.child_element(item, "enclosure")
    set_img_attrs(enclosure, IMG)
    thumbnail = xtree.child_element(item, "media:thumbnail")
    set_img_attrs(thumbnail, IMG)
    media = xtree.child_element(item, "media:content")
    set_img_attrs(media, IMG)

    return item

def set_img_attrs(elem, img):
    """
    Adds XML attributes to RSS image elements
    """
    elem_tag = elem.tag
    xtree.set_attribute(elem, "url", img)

    if elem_tag == "enclosure":
        xtree.set_attribute(elem, "type", "image/jpeg")
        xtree.set_attribute(elem, "length", "0")
    elif elem_tag == "media:thumbnail":
        xtree.set_attribute(elem, "width", "1920")
        xtree.set_attribute(elem, "height", "1080")
    elif elem_tag == "media:content":
        xtree.set_attribute(elem, "type", "image/jpeg")

    return elem

from utils import xtree
from utils.files import path_to_url

NAMESPACES = [
        "http://www.sitemaps.org/schemas/sitemap/0.9"
        ]

def build_sitemap(doc_tree):
    urlset = xtree.root_element(NAMESPACES, "urlset")
    for doc in doc_tree:
        url = xtree.child_element(urlset, "url")
        loc_text = path_to_url(doc)
        loc = xtree.child_element(url, "location", loc_text)
    return urlset

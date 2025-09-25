from utils import xtree
from utils.files import path_to_url

NAMESPACES = [
        "http://www.sitemaps.org/schemas/sitemap/0.9"
        ]

def sort_tree(tree):
    tree.sort()
    tree.sort(key=lambda doc: doc.count('/'))
    return tree

def build_sitemap(doc_tree):
    path_tree = [path_to_url(doc) for doc in doc_tree]
    sort_tree(path_tree)
    urlset = xtree.root_element(NAMESPACES, "urlset")
    for doc in path_tree:
        url = xtree.child_element(urlset, "url")
        #loc_text = path_to_url(doc)
        #loc = xtree.child_element(url, "location", loc_text)
        loc = xtree.child_element(url, "location", doc)
    return urlset

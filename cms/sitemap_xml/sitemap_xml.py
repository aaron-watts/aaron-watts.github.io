from utils import xtree
from utils.files import path_to_url

NAMESPACES = [
        "http://www.sitemaps.org/schemas/sitemap/0.9"
        ]

def sort_tree(tree):
    """
    Return document tree by folder with index's first
    """
    tree.sort()
    tree.sort(key=lambda doc: doc.count('/'))
    return tree

def build_sitemap(doc_tree):
    """
    Return sitemap xml tree object
    """
    path_tree = [path_to_url(doc) for doc in doc_tree]
    path_tree = sort_tree(path_tree)
    urlset = xtree.root_element(NAMESPACES, "urlset")
    for doc in path_tree:
        url = xtree.child_element(urlset, "url")
        loc = xtree.child_element(url, "location", doc)
    return urlset

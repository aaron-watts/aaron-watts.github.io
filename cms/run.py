#!/usr/bin/env python3

"""Run CMS scripts to build aaronwatts.dev"""

from utils.files import get_articles, get_docs, write_to_xml
from doc_test.doc_test import test_documents
from sitemap_xml.sitemap_xml import build_sitemap

if __name__ == "__main__":
    print("Build aaronwatts.dev")

    # get all files
    articles = get_articles()
    # test
    TESTS_PASSED = test_documents(articles)

    doc_tree = get_docs()

    sitemap = build_sitemap(doc_tree)
    write_to_xml(sitemap, 'xml_test/sitemap.xml')

    # articles
    # feeds

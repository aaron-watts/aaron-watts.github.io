#!/usr/bin/env python3

"""Run CMS scripts to build aaronwatts.dev"""

import config.config as config
from utils.files import get_articles, get_docs, write_to_xml
from doc_test.doc_test import test_documents
from sitemap_xml.sitemap_xml import build_sitemap
from rss_xml.rss_xml import build_rss

if __name__ == "__main__":
    print("Build aaronwatts.dev")

    config = config.settings

    articles = get_articles()
    TESTS_PASSED = test_documents(articles)

    if TESTS_PASSED:
        doc_tree = get_docs()

        sitemap = build_sitemap(doc_tree)
        write_to_xml(sitemap, config['sitemap']['path'])

        # feeds
        rss = build_rss(articles)
        write_to_xml(rss, config['feeds']['all']['path'])
        # articles

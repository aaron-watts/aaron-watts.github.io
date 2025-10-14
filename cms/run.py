#!/usr/bin/env python3

"""Run CMS scripts to build aaronwatts.dev"""

from config.settings import ROOT, HOME, SUB_DIRECTORIES, SITEMAP, FEEDS
from utils.files import get_articles, get_docs, write_to_xml, write_to_html
from utils.soup import extract_data
from doc_test.doc_test import test_documents
from sitemap_xml.sitemap_xml import build_sitemap
from rss_xml.rss_xml import build_rss
from content_pages.content_pages import home_page, index_page

if __name__ == "__main__":
    print("Build aaronwatts.dev")

    articles = get_articles()
    TESTS_PASSED = test_documents(articles)

    if TESTS_PASSED:
        doc_tree = get_docs()

        sitemap = build_sitemap(doc_tree)
        write_to_xml(sitemap, SITEMAP['path'])

        for article in articles:
            article = extract_data(article)

        articles.sort(
                key=lambda article: article['date'],
                reverse=True
                )

        rss = build_rss(articles)
        write_to_xml(rss, FEEDS['all']['path'])

        home_html = home_page(articles[0])
        write_to_html(home_html, f"xml_test/{HOME}")

        filtered_articles = {}
        for sub_dir in SUB_DIRECTORIES:
            filtered = filter(
                    lambda article: article['directory'] == sub_dir,
                    articles
                    )
            filtered_articles[sub_dir] = list(filtered)

            feed = build_rss(filtered_articles[sub_dir])
            write_to_xml(feed, FEEDS[sub_dir]['path'])

            index_html = index_page(
                    filtered_articles[sub_dir],
                    f"{ROOT}/{sub_dir}/index.html"
                    )
            write_to_html(index_html, f"xml_test/{sub_dir}/index.html")

        # articles

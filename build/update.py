#!/usr/bin/env python3

"""Update aaronwatts.dev feeds, sitemap and home/index pages"""

import sitemap
import articles
import feeds

if __name__ == "__main__":
    print('Updating sitemap.xml\n...')
    sitemap.main()
    print('Updating home and indexes\n...')
    articles.main()
    print('Updating RSS feeds\n...')
    feeds.main()
    print('Update complete')

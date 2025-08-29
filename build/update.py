#!/usr/bin/env python3

"""Update aaronwatts.dev feeds, sitemap and home/index pages"""

import sys
import sitemap
import articles
import feeds

sys.path.insert(1, './test')
from test import run_tests

if __name__ == "__main__":
    tests_passed = run_tests()
    if tests_passed is True:
        print("All tests passed, proceeding with build operation")
        print('Updating sitemap.xml\n...')
        #sitemap.main()
        print('Updating home and indexes\n...')
        #articles.main()
        print('Updating RSS feeds\n...')
        #feeds.main()
        print('Update complete')
    else:
        print('Build operation terminated due to failed test(s)')


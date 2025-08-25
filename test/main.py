#!/usr/bin/env python3

"""Testing for aaronwatts.dev articles"""

# Tests:
# main element does not contain comments
# main > img contains href
# main > img contains alt
# nav a all have corresponding h2[id=href]
# h1 contains text
# time element datetime confirms to yyyy-mm-dd
# datetime innerhtml conforms to dd<sup>aa</sup> MMM, YYYY
# main > p:first-of-type has id="intro"
# nav.breadcrumbs.replace(/aaronwatts@dev:| \$/g, '') = dir/filename
# script > initComments > commentSectionId has original id not already used
# meta[name="description"] is not blank
# meta[name="keywords"] is not blank

if __name__ == "__main__":
    print("We are in test/main.py")

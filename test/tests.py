#1/usr/bin/env python3

"""Tests to conduct on aaronwatts.dev articles"""

import os
import re
from bs4 import Comment

def comments_has_id(html_doc):
    """
    commentSectionID is present in script tag
    """
    script = html_doc["soup"].select_one("body > script").string
    result = re.search(r'commentSectionId: "\S+"', script)
    if result is None:
        print(f"TEST FAILED: No comment section ID in {html_doc['path']}")
        return False
    print("TEST PASSED: comment section ID present")
    return False

def keywords_not_blank(html_doc):
    """
    meta keywords is not blank
    """
    keywords = html_doc["soup"].select_one("meta[name='keywords']")["content"]
    if len(keywords) > 0:
        print("TEST PASSED: meta keywords is not blank")
        return True
    print(f"TEST FAILED: meta keywords is blank in {html_doc['path']}")
    return False

def description_not_blank(html_doc):
    """
    meta description is not blank
    """
    desc = html_doc["soup"].select_one("meta[name='description']")["content"]
    if len(desc) > 0:
        print("TEST PASSED: meta description is not blank")
        return True
    print(f"TEST FAILED: meta description is blank in {html_doc['path']}")
    return False

def breadcrumb_matches_path(html_doc):
    """
    nav breadcrumb matches path
    """
    breadcrumb = html_doc["soup"].select_one("nav.breadcrumbs").text
    breadcrumb_trail = re.sub(r"aaronwatts@dev:| \$", '', breadcrumb)
    breadcrumb_path = "docs" + breadcrumb_trail.strip() +".html"
    if not breadcrumb_path == html_doc['path']:
        print(f"TEST FAILED: breadcrumb does not match path in {html_doc['path']}")
        return False
    print("TEST PASSED: breadcrumb matches path")
    return True


def intro_is_included(html_doc):
    """
    First p element has id of intro
    """
    intro = html_doc["soup"].select_one("main > p:first-of-type")
    if not intro["id"] == "intro":
        print(f"TEST FAILED: intro does not have id of intro in {html_doc['path']}")
        return False
    print("TEST PASSED: intro has id of intro")
    return True

def time_innerhtml_formatted(html_doc):
    """
    time element innerHTML conforms to D MMM, yyyy
    """
    time_text = html_doc["soup"].select_one("time").text
    result = re.search(r"\d{1,2}\w{2}\s\w{3,8},\s\d{4}", time_text)
    if result is None:
        print(f"TEST FAILED: date inneirText formatted incorrectly in {html_doc['path']}")
        return False
    print("TEST PASSED: date innerText foratted correctly")
    return True

def time_datetime_formatted(html_doc):
    """
    time elements datetime attribute is correctly formatted
    """
    datetime = html_doc["soup"].select_one("time")["datetime"]
    result = re.search(r"\d{4}-\d{2}-\d{2}", datetime)
    if result is None:
        error_msg = "TEST FAILED: time element datetime attr"
        error_msg += " does not conform to yyyy-mm-dd in "
        error_msg += html_doc["path"]
        print(error_msg)
        return False
    print("TEST PASSED: time elements datetime attribute conforms to yyyy-mm-dd")
    return True

def h1_has_text(html_doc):
    """
    h1 contains text
    """
    header1 = html_doc["soup"].select_one("main > h1")
    if len(header1.text) == 0:
        print(f"TEST FAILED: h1 is blank in {html_doc['path']}")
        return False
    print("TEST PASSED: h1 has text")
    return True

def nav_anchors_have_targets(html_doc):
    """
    nav anchors have corresponding targets
    """
    passed = True
    if html_doc["parent_dir"] == "tech":
        print("TEST NOT REQUIRED: No page nav for tech articles")
        return True
    nav_links = html_doc["soup"].select("nav li > a")
    for nav_link in nav_links:
        href = nav_link["href"]
        targets = html_doc["soup"].select(href)
        target_n = len(targets)
        if target_n == 0:
            print(f"TEST FAILED: Too many targets for href ${href} in ${html_doc['path']}")
            passed = False
        if target_n > 1:
            print(f"TEST FAILED: No target for href ${href} in ${html_doc['path']}")
            passed = False
    if not passed:
        return False
    print("TEST PASSED: hrefs for page headers all have targets")
    return True

def img_exists(html_doc):
    """
    img src exists in images folder
    """
    img_src = html_doc["soup"].select_one("main > img")["src"]
    if os.path.exists(f"docs/{img_src}"):
        print("TEST PASSED: img src exists in docs/images")
        return True
    print(f"FAILED TEST: img src does not exist in docs/images for {html_doc['path']}")
    return False

def main_img_alt(html_doc):
    """
    Article image has alt text
    """
    img = html_doc["soup"].select_one("main > img")
    alt = img["alt"]
    if len(alt) == 0:
        print(f"FAILED TEST: img has no alt text in {html_doc['path']}")
        return False
    print("TEST PASSED: img has alt text")
    return True

def main_img_rsc(html_doc):
    """
    Article images has href
    """
    img = html_doc["soup"].select_one("main > img")
    src = img["src"]
    if len(src) == 0:
        print(f"FAILED TEST: img has no src in {html_doc['path']}")
        return False
    print("TEST PASSED: img has src")
    return True

def no_comments(html_doc):
    """
    HTML doc contains no comments
    """
    comments = html_doc["soup"].find_all(string=lambda text: isinstance(text, Comment))
    if len(comments) > 0:
        print(f"FAILED TEST: comments in doc in {html_doc['path']}")
        return False
    print("TEST PASSED: No comments in doc")
    return True

tests = [
        no_comments,
        main_img_rsc,
        main_img_alt,
        img_exists,
        nav_anchors_have_targets,
        h1_has_text,
        time_datetime_formatted,
        time_innerhtml_formatted,
        intro_is_included,
        breadcrumb_matches_path,
        description_not_blank,
        keywords_not_blank,
        comments_has_id
        ]

#1/usr/bin/env python3

"""Tests to conduct on aaronwatts.dev articles"""

import os
import re
from bs4 import Comment

def comments_has_id(html_doc):
    """
    commentSectionID is present in script tag
    """
    result = {}
    script = html_doc["soup"].select_one("body > script").string
    test = re.search(r'commentSectionId: "\S+"', script)
    if test is None:
        result["msg"] = "FAILED: Comment config has ID"
        result["passed"] = False
    else:
        result["msg"] = "PASSED: Comment config has ID"
        result["passed"] = True
    print(result["msg"])
    return result

def keywords_not_blank(html_doc):
    """
    meta keywords is not blank
    """
    result = {}
    keywords = html_doc["soup"].select_one("meta[name='keywords']")["content"]
    if len(keywords) > 0:
        result["msg"] = "PASSED: meta keywords is not blank"
        result["passed"] = True
    else:
        result["msg"] = "FAILED: meta keywords is blank" 
        result["passed"] = False
    print(result["msg"])
    return result

def description_not_blank(html_doc):
    """
    meta description is not blank
    """
    result = {}
    desc = html_doc["soup"].select_one("meta[name='description']")["content"]
    if len(desc) > 0:
        result["msg"] = "PASSED: meta description is not blank"
        result["passed"] = True
    else:
        result["msg"] = "FAILED: meta description is blank"
        result["passed"] = False
    print(result["msg"])
    return result

def breadcrumb_matches_path(html_doc):
    """
    nav breadcrumb matches path
    """
    result = {}
    breadcrumb = html_doc["soup"].select_one("nav.breadcrumbs").text
    breadcrumb_trail = re.sub(r"aaronwatts@dev:| \$", '', breadcrumb)
    breadcrumb_path = "docs" + breadcrumb_trail.strip() +".html"
    if not breadcrumb_path == html_doc['path']:
        result["msg"] = "FAILED: breadcrumb does not match path"
        result["passed"] = False
    else:
        result["msg"] = "PASSED: Breadcrumb matches path"
        result["passed"] = True
    print(result["msg"])
    return result

def intro_is_included(html_doc):
    """
    First p element has id of intro
    """
    result = {}
    intro = html_doc["soup"].select_one("main > p:first-of-type")
    if not intro["id"] == "intro":
        result["msg"] = "FAILED: Intro does not have id of intro"
        result["passed"] = False
    else:
        result["msg"] = "PASSED: Intro has id of intro"
        result["passed"] = True
    print(result["msg"])
    return result

def time_innerhtml_formatted(html_doc):
    """
    time element innerHTML conforms to D MMM, yyyy
    """
    result = {}
    time_text = html_doc["soup"].select_one("time").text
    test = re.search(r"\d{1,2}\w{2}\s\w{3,8},\s\d{4}", time_text)
    if test is None:
        result["msg"] = "FAILED: date innerText formatted incorrectly"
        result["passed"] = False
    else:
        result["msg"] = "PASSED: date innerText foratted correctly"
        result["passed"] = True
    print(result["msg"])
    return result

def time_datetime_formatted(html_doc):
    """
    time elements datetime attribute is correctly formatted
    """
    result = {}
    datetime = html_doc["soup"].select_one("time")["datetime"]
    test = re.search(r"\d{4}-\d{2}-\d{2}", datetime)
    if test is None:
        result["msg"] = "FAILED: datetime attribute not yyyy-mm-dd"
        result["passed"] = False
    else:
        result["msg"] = "PASSED: datetime attribute is yyyy-mm-dd"
        result["passed"] = True
    print(result["msg"])
    return result

def h1_has_text(html_doc):
    """
    h1 contains text
    """
    result = {}
    header1 = html_doc["soup"].select_one("main > h1")
    if len(header1.text) == 0:
        result["msg"] = "FAILED: h1 is blank"
        result["passsed"] = False
    else:
        result["msg"] = "PASSED: H1 is not blank"
        result["passed"] = True
    print(result["msg"])
    return result

def nav_anchors_have_targets(html_doc):
    """
    nav anchors have corresponding targets
    """
    result = {}
    test = True
    if html_doc["parent_dir"] == "tech":
        result["msg"] = "OMITTED: tech pages do not use nav"
        result["passed"] = True
        print(result["msg"])
        return result
    nav_links = html_doc["soup"].select("nav li > a")
    for nav_link in nav_links:
        href = nav_link["href"]
        targets = html_doc["soup"].select(href)
        target_n = len(targets)
        if target_n == 0 or target_n > 1:
            test = False
    if test:
        result["msg"] = "PASSED: Nav links have corresponding headings"
        result["passed"] = True
    else:
        result["msg"] = "FAILED: Nav links do not have corresponding headings"
        result["passed"] = True
    print(result["msg"])
    return result

def img_exists(html_doc):
    """
    img src exists in images folder
    """
    result = {}
    img_src = html_doc["soup"].select_one("main > img")["src"]
    if os.path.exists(f"docs/{img_src}"):
        result["msg"] = "PASSED: img src exists in docs/images"
        result["passed"] = True
    else:
        result["msg"] = "FAILED: Img src does not exist in docs/images"
        result["passed"] = False
    print(result["msg"])
    return result

def main_img_alt(html_doc):
    """
    Article image has alt text
    """
    result = {}
    img = html_doc["soup"].select_one("main > img")
    alt = img["alt"]
    if len(alt) == 0:
        result["msg"] = "FAILED: img has no alt text"
        result["passed"] = False
    else:
        result["msg"] = "PASSED: img has alt text"
        result["passed"] = True
    print(result["msg"])
    return result

def main_img_rsc(html_doc):
    """
    Article images has href
    """
    result = {}
    img = html_doc["soup"].select_one("main > img")
    src = img["src"]
    if len(src) == 0:
        result["msg"] = "FAILED: img has no src"
        result["passed"] = False
    else:
        result["msg"] = "PASSED: img has src"
        result["passed"] = True
    print(result["msg"])
    return result

def no_comments(html_doc):
    """
    HTML doc contains no comments
    """
    result = {}
    comments = html_doc["soup"].find_all(string=lambda text: isinstance(text, Comment))
    if len(comments) > 0:
        result["msg"] = "FAILED: comments in doc"
        result["passed"] = False
    else:
        result["msg"] = "PASSED: no comments in doc"
        result["passed"] = True
    print(result["msg"])
    return result

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

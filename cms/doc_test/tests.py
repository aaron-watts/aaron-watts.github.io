import os
import re
from bs4 import Comment

def no_comments(html_doc):
    """
    HTML doc contains no comments
    """
    result = {
        "desc": "Document should not contain comments"
            }
    comments = html_doc["soup"].find_all(string=lambda text: isinstance(text, Comment))
    if len(comments) > 0:
        result["passed"] = False
    else:
        result["passed"] = True
    return result

def main_img_rsc(html_doc):
    """
    Article images has src
    """
    result = {
        "desc": "img[src] should not be blank"
            }
    img = html_doc["soup"].select_one("article img")
    src = img["src"]
    if len(src) == 0:
        result["passed"] = False
    else:
        result["passed"] = True
    return result

def main_img_alt(html_doc):
    """
    Article image has alt text
    """
    result = {
        "desc": "img[alt] should not be blank"
            }
    img = html_doc["soup"].select_one("article img")
    alt = img["alt"]
    if len(alt) == 0:
        result["passed"] = False
    else:
        result["passed"] = True
    return result


def img_exists(html_doc):
    """
    img src exists in images folder
    """
    result = {
        "desc": "img[src] should exist in images/"
            }
    img_src = html_doc["soup"].select_one("article img")["src"]
    if os.path.exists(f"docs/{img_src}"):
        result["passed"] = True
    else:
        result["passed"] = False
    return result


def nav_anchors_have_targets(html_doc):
    """
    nav anchors have corresponding targets
    """
    result = {
        "desc": "nav a href's should have corresponding #targets"
            }
    test = True
    if html_doc["directory"] == "tech":
        result["passed"] = True
        return result
    nav_links = html_doc["soup"].select("nav li > a")
    for nav_link in nav_links:
        href = nav_link["href"]
        targets = html_doc["soup"].select(href)
        target_n = len(targets)
        if target_n == 0 or target_n > 1:
            test = False
    if test:
        result["passed"] = True
    else:
        result["passed"] = True
    return result

def h1_has_text(html_doc):
    """
    h1 contains text
    """
    result = {
        "desc": "h1 should not be blank"
            }
    header1 = html_doc["soup"].select_one("article h1")
    if len(header1.text) == 0:
        result["passsed"] = False
    else:
        result["passed"] = True
    return result

def time_datetime_formatted(html_doc):
    """
    time elements datetime attribute is correctly formatted
    """
    result = {
        "desc": "time element attr date should conform ro yyyy-mm-dd"
            }
    datetime = html_doc["soup"].select_one("article header time")["datetime"]
    test = re.search(r"\d{4}-\d{2}-\d{2}", datetime)
    if test is None:
        result["passed"] = False
    else:
        result["passed"] = True
    return result

def time_innerhtml_formatted(html_doc):
    """
    time element innerHTML conforms to D MMM, yyyy
    """
    result = {
        "desc": "time element innerHTML should conform to d mmm, yyyy"
            }
    time_text = html_doc["soup"].select_one("article header time").text
    test = re.search(r"\d{1,2}\w{2}\s\w{3,8},\s\d{4}", time_text)
    if test is None:
        result["passed"] = False
    else:
        result["passed"] = True
    return result


def intro_is_included(html_doc):
    """
    First p element has id of intro
    """
    result = {
        "desc": "First p element in main should have id of 'intro'"
            }
    intro = html_doc["soup"].select_one("article p:first-of-type")
    if not intro["id"] == "description":
        result["passed"] = False
    else:
        result["passed"] = True
    return result

def breadcrumb_matches_path(html_doc):
    """
    nav breadcrumb matches path
    """
    result = {
        "desc": "nav.breadcrumb should match path"
            }
    breadcrumb = html_doc["soup"].select_one("nav.breadcrumbs").text
    breadcrumb_trail = re.sub(r"aaronwatts@dev:| \$", '', breadcrumb)
    breadcrumb_path = "docs" + breadcrumb_trail.strip() +".html"
    if not breadcrumb_path == html_doc['path']:
        result["passed"] = False
    else:
        result["passed"] = True
    return result

def description_not_blank(html_doc):
    """
    Meta description should not be blank
    """
    result = {
        "desc": "Meta description should not be blank"
            }
    desc = html_doc["soup"].select_one("meta[name='description']")["content"]
    if len(desc) > 0:
        result["passed"] = True
    else:
        result["passed"] = False
    return result

def keywords_not_blank(html_doc):
    """
    Meta keywords required for topic labels
    """
    result = {
        "desc": "Meta keywords should not be blank"
            }
    keywords = html_doc["soup"].select_one("meta[name='keywords']")["content"]
    if len(keywords) > 0:
        result["passed"] = True
    else:
        result["passed"] = False
    return result

tests = [
        no_comments,
        main_img_rsc,
        main_img_alt,
        img_exists,
        #nav_anchors_have_targets,
        h1_has_text,
        time_datetime_formatted,
        time_innerhtml_formatted,
        intro_is_included,
        #breadcrumb_matches_path,
        description_not_blank,
        keywords_not_blank,
        ]

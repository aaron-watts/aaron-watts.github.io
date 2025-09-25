import os
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

ROOT_DIR = "docs"
ARTICLE_DIRS = ["guides", "tech"]

def path_to_url(file_path):
    file_path = file_path.replace("index.html", "")
    file_path = file_path.replace(".html", "")
    file_path = re.sub(r"\W+^", "", file_path)
    url = f"https://aaronwatts.dev/{file_path}"
    return url

def file_valid(file_name):
    if file_name.endswith(".html"):
        return True
    return False

def get_articles():
    articles = []
    for directory in ARTICLE_DIRS:
        for file in os.scandir(f"{ROOT_DIR}/{directory}"):
            if file_valid(file.name) and not file.name == "index.html":
                full_path = f"{ROOT_DIR}/{directory}/{file.name}"
                with open(full_path) as html_doc:
                    soup = BeautifulSoup(html_doc, "lxml")
                    article_doc = {
                        "filename": file.name,
                        "directory": directory,
                        "path": full_path,
                        "soup": soup
                            }
                    articles.append(article_doc)
    return articles

def get_docs():
    docs = []
    include_root = [""] + ARTICLE_DIRS
    for directory in include_root:
        for file in os.scandir(f"{ROOT_DIR}/{directory}"):
            if file_valid(file.name):
                dir_name = directory
                if len(dir_name) > 0:
                    dir_name = dir_name + "/"
                docs.append(f"{dir_name}{file.name}")
    return docs

def write_to_xml(xml_tree, path):
    tree = ET.ElementTree(xml_tree)
    ET.indent(tree)
    tree.write(path, xml_declaration="version", encoding="UTF-8")

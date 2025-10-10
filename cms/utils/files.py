import os
import re
from config.settings import ROOT, BASE_URL, SUB_DIRECTORIES
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


def get_docs():
    """
    Return list of all HTML files as list of strings
    """
    docs = []
    include_root = [""] + SUB_DIRECTORIES
    for directory in include_root:
        for file in os.scandir(f"{ROOT}/{directory}"):
            if file_valid(file.name):
                dir_name = directory
                if len(dir_name) > 0:
                    dir_name = dir_name + "/"
                docs.append(f"{dir_name}{file.name}")
    return docs


def get_articles():
    """
    Return list of HTML articles as dict's
    """
    articles = []
    for directory in SUB_DIRECTORIES:
        for file in os.scandir(f"{ROOT}/{directory}"):
            if file_valid(file.name) and not file.name == "index.html":
                full_path = f"{ROOT}/{directory}/{file.name}"
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


def write_to_xml(xml_tree, path):
    """
    Write XML tree to path
    """
    tree = ET.ElementTree(xml_tree)
    ET.indent(tree)
    tree.write(path, xml_declaration="version", encoding="UTF-8")


def file_valid(file_name):
    """
    Check if file is HTML and return boolean
    """
    if file_name.endswith(".html"):
        return True
    return False


def path_to_url(file_path):
    """
    Convert file path to url and return as string
    """
    file_path = file_path.replace("index.html", "")
    file_path = file_path.replace(".html", "")
    file_path = re.sub(r"\W+^", "", file_path)
    url = f"{BASE_URL}/{file_path}"
    return url


def image_url_from_file(file):
    """
    Returns img url based on file and path
    """ 
    img_url = f"{BASE_URL}/images/"
    img_url += f"{file['directory']}/"
    img_url += file['filename'].replace(".html", ".jpg")
    return img_url

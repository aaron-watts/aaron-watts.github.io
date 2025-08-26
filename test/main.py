#!/usr/bin/env python3

"""Testing for aaronwatts.dev articles"""

import os
from tests import tests
from bs4 import BeautifulSoup


def file_valid(file_name):
    """Check if file valid for tests"""
    if file_name == "index.html":
        return False
    if file_name.endswith(".xml"):
        return False
    if file_name.endswith(".swp"):
        return False
    return True

def main():
    """Main Function"""
    sub_directories = [
        "guides",
        "tech"
    ]

    for directory in sub_directories:
        for file in os.scandir(f"docs/{directory}"):
            if file_valid(file.name):
                full_path = f"docs/{directory}/{file.name}"
                with open(full_path) as html_doc:
                    soup = BeautifulSoup(html_doc, "lxml")
                config = {
                    "filename": file.name,
                    "parent_dir": directory,
                    "path": full_path,
                    "soup": soup
                }
                print(f"Testing {full_path}...")
                for test in tests:
                    test(config)

if __name__ == "__main__":
    main()

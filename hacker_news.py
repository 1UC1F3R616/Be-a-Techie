#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen

def work():
    print("news.ycombinator.com")
    url = "https://news.ycombinator.com/"
    file = urlopen(url)
    page = file.read()
    file.close()
    page_soup = BeautifulSoup(page, "html.parser")
    container = page_soup.findAll("a", {"class":"storylink"})
    print("\n\n")
    for getter in container:
        print(getter.text)
    print("\n\n")

if __name__ == "__main__":
    work()

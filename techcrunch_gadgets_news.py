#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen

def work():
    print("www.techcrunch.com--> Startups")
    url = "https://techcrunch.com/startups/"
    file = urlopen(url)
    page = file.read()
    file.close()
    page_soup = BeautifulSoup(page, "html.parser")
    container = page_soup.findAll("a", {"class":"post-block__title__link"})
    print("\n\n")
    for getter in container:
        print(getter.text)
    print("\n\n")

if __name__ == "__main__":
    work()

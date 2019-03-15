# -*- coding: utf-8 -*-
#! /usr/bin/env python


import daily_hack_news as dhn
import hacker_news
import techcrunch_gadgets_news as tgd
import techcrunch_startups_news as tsd
from tkinter import *


def but1():
    dhn.work()
def but2():
    hacker_news.work()
def but3():
    tgd.work()
def but4():
    tsd.work()


root = Tk()
root.geometry("600x150")
root.title("Tech News 4 Techies")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

label1 = Label(topFrame, text="Be a Techie!", bg="pale green", font = "Symbol", relief="groove")
label1.pack(side=TOP, fill='x', expand=True)

b1 = Button(bottomFrame, text="Hack News", bg="PaleTurquoise1", fg="red", cursor="star", command=but1)
b2 = Button(bottomFrame, text="Hacker News", bg="PaleTurquoise1", fg="red", cursor="star", command=but2)
b3 = Button(bottomFrame, text="Techcrunch Gadgets", bg="PaleTurquoise1", fg="red", cursor="star", command=but3)
b4 = Button(bottomFrame, text="Techcrunch Startups", bg="PaleTurquoise1", fg="red", cursor="star", command=but4)

b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)
b4.pack(side = LEFT)

root.mainloop()

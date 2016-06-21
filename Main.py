#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import requests
from bs4 import BeautifulSoup
import bs4
import os
import sys
import webbrowser
sys.path.append("libs")

reload(sys)
sys.setdefaultencoding( "utf-8" )

def sodu(searchText):
    r = requests.get("http://www.sodu.cc/result.html?searchstr=" + searchText)
    soup = BeautifulSoup(r.text,"lxml")
    for child in soup.find_all('a'):
        # uncode编码警告：在unicode等价比较中，把两个参数同时转换为unicode编码失败。中断并认为他们不相等。
        # python里一般处理的是unicode和str的文本对象，经过侦测，传给chardet的文本是“ascii”的的格式，所以传给chardet前先转成unicode的就好了。
        if child.string == searchText.decode("utf-8"):
            searchHtmlList(child['href'])
            break

def searchHtmlList(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    for child in soup.find_all('a'):
        if child.has_key('alt'):
            if type(child.string) != None :
                try:
                    # saveHtmlData(child.string,child['href'].split('chapterurl=')[1])
                    print child.string + " " + child['href']
                    listb.insert(0, child.string + " " + child['href'])
                    # print '\n'
                except Exception, ex:
                    print Exception,":",ex

def searchNovel():
    text = u.get();
    print text
    sodu(text)

def jump_html(arg):
    content = listb.get(listb.curselection())
    array = content.split(' ')
    url = array[len(array) - 1]
    print url
    webbrowser.open(url)

if __name__ == '__main__':
    # 导入 Tkinter 库
    root = Tk()

    root.title("小说查找工具")
    root.geometry('1000x600')

    label = Label(root,text="请输入要搜索的小说?")

    u = StringVar()
    entry = Entry(root, textvariable=u)
    btn = Button(root,text="搜索",
                 command=searchNovel)
    listb = Listbox(root,width=900,height=600)

    listb.bind('<ButtonRelease-1>', jump_html)

    label.pack()
    entry.pack()
    btn.pack()
    listb.pack()

    # 进入消息循环
    root.mainloop()
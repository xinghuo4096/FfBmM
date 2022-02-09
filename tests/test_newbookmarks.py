import codecs
import copy
import datetime
import json
import os
import sys
import time

import firefoxbookmarks
from firefoxbookmarks.MozBaseItem import MozBaseItem

a = os.getcwd()
b = os.getenv('pythonpath')
c = sys.path


def test_newuuid():
    name = "test"
    str1 = firefoxbookmarks.getguid(name)
    assert len(str1) > 0
    assert len(str1) == 12


def test_newfolder():

    a = float('1643120121073000') / (pow(10, 6))
    t = time.localtime(a)
    s1 = time.strftime("%Y-%m-%d %H:%M:%S", t)
    assert s1 == '2022-01-25 22:15:21'

    dt = datetime.datetime.fromtimestamp(a)
    s1 = dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    assert s1 == '2022-01-25 22:15:21.073000'

    name = "newFolder"
    folder = firefoxbookmarks.newfolder(name, 1, 2)
    assert isinstance(folder, firefoxbookmarks.MozPlaceContainer)
    assert isinstance(folder, firefoxbookmarks.MozBaseItem)
    assert len(folder.guid) > 0
    assert len(folder.guid) == 12
    assert len(str(folder.dateAdded)) == 16
    assert len(str(folder.lastModified)) == 16


def test_addbookmark():
    bms = loadbms()
    root = bms.root
    assert isinstance(root, firefoxbookmarks.MozPlaceContainer)
    assert root.guid == 'root________'
    assert root.root == 'placesRoot'

    menu = root.children[0]
    assert isinstance(menu, firefoxbookmarks.MozPlaceContainer)
    assert menu.title == 'menu'

    news = menu.children[0]
    assert isinstance(news, firefoxbookmarks.MozPlaceContainer)
    assert isinstance(news.title, str)
    assert news.title.lower() == 'news'

    bd = news.children[0]
    assert isinstance(bd, firefoxbookmarks.MozPlace)
    assert isinstance(bd.uri, str)
    assert bd.uri.lower() == 'http://news.baidu.com/'


def test_addBookmark():

    bms = loadbms()
    root = bms.root
    assert isinstance(root, firefoxbookmarks.MozPlaceContainer)
    maxid = bms.MaxBookmarksId()

    name = "newFolder"
    maxid += 1
    folder = firefoxbookmarks.newfolder(name, 1, maxid)
    menu = root.children[0]

    news = menu.children[0]
    bd = news.children[0]
    assert isinstance(bd, MozBaseItem)

    bd2 = copy.deepcopy(bd)
    maxid += 1
    bd2.id = maxid
    bd2.guid=firefoxbookmarks.getguid(bd2.uri)
    folder.AddChildern(bd2)
    if (isinstance(menu, firefoxbookmarks.MozPlaceContainer)):
        menu.AddChildern(folder)
        pass
    #menu.AddChildern(bd2)
    js = bms.root
    s1 = root.toJSON()
    js3 = s1  
     

    path2 = "outdata/new-bookmarks-test.json"
    f = codecs.open(path2, "w", "utf-8")
    s = f.write(js3)
    f.close()
    assert len(js3) > 0




def loadbms() -> firefoxbookmarks.Manager:
    s1 = os.getcwd()
    path2 = "tests/bookmarks-test.json"
    f = codecs.open(path2, "r", "utf-8")
    s = f.read()
    f.close()
    assert len(s) > 0
    bms = firefoxbookmarks.Manager()
    bms.Json2Bookmarks(s)
    return bms


# --------------
test_addBookmark()

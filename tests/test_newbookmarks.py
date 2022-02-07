import codecs
import datetime
import os
import sys
import time

import firefoxbookmarks

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
    assert len(folder.date_added) == 16
    assert len(folder.last_modified) == 16


def test_addbookmark():
    bms = loadbms()
    root = bms.root
    assert isinstance(root, firefoxbookmarks.MozPlaceContainer)
    assert root.title == 'root________'
    assert root.guid == 'placesRoot'

    menu = root.children[0]
    assert isinstance(menu, firefoxbookmarks.MozPlaceContainer)
    assert menu.title == 'menu'

    news = menu.children[0]
    assert isinstance(news, firefoxbookmarks.MozPlaceContainer)
    assert isinstance(news.title, str)
    assert news.title.lower == 'news'

    bd = news.children[0]
    assert isinstance(bd, firefoxbookmarks.MozPlace)
    assert isinstance(bd.uri, str)
    assert news.uri.lower == 'http://news.baidu.com/'

    # TODO 增加文件夹，增加书签


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

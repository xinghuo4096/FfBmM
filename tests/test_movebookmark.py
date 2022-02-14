import codecs

import os
import firefoxbookmarks
from firefoxbookmarks.MozBaseItem import MozBaseItem
from firefoxbookmarks.MozPlace import MozPlace
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer


def test_movebm():
    bms = loadbms()
    root = bms.root
    bms.AddTagsToBookmark(root, '')

    root = bms.root
    folder = root

    assert isinstance(root, MozPlaceContainer)
    assert isinstance(folder, MozPlaceContainer)
    assert root is folder

    menu = folder.children[0]

    news = menu.children[0]
    assert isinstance(folder, MozPlaceContainer)
    assert news.title.lower() == 'news'

    bd = news.children[0]
    assert isinstance(bd, MozPlace)
    assert bd.uri == 'http://news.baidu.com/'
    assert 'news' in bd.tags.lower()

    assert '百度新闻' in bd.title

    bms2 = bms.movefunc_without_folder(findstr='baidu')
    bms2root = bms2.root

    assert isinstance(root, MozPlaceContainer)
    assert isinstance(bms2root, MozPlaceContainer)
    assert root is folder

    menu = folder.children[0]

    news = menu.children[0]
    assert isinstance(folder, MozPlaceContainer)
    assert news.title.lower() == 'news'

    sina = news.children[0]
    assert isinstance(sina, MozPlace)
    assert sina.uri == 'https://news.sina.com.cn/'
    assert 'news' in sina.tags.lower()
    print(sina.tags.lower())
    assert '新浪网' in sina.title


def test_movefunc_without_folder():
    bms = loadbms()

    root = bms.root
    assert isinstance(root, MozPlaceContainer)
    menu = root.children[0]
    assert isinstance(menu, MozPlaceContainer)
    assert menu.title == 'menu'

    天气 = menu.children[1]
    assert isinstance(天气, MozPlaceContainer)
    assert 天气.title == '天气'

    历史天气 = 天气.children[3]
    assert isinstance(历史天气, MozPlaceContainer)
    assert 历史天气.title == '历史天气'
    assert len(历史天气.children) == 2

    tq1 = 历史天气.children[0]
    tq2 = 历史天气.children[1]
    assert isinstance(tq1, MozPlace)
    assert isinstance(tq2, MozPlace)
    assert '保定1月份天气' in tq1.title
    assert '北京历史气温' in tq2.title

    bms.movefunc_without_folder(findstr='tianqi.com')
    assert isinstance(bms.root, MozPlaceContainer)

    root = bms.root
    assert isinstance(root, MozPlaceContainer)
    menu = root.children[0]
    assert isinstance(menu, MozPlaceContainer)
    assert menu.title == 'menu'

    天气 = menu.children[1]
    assert isinstance(天气, MozPlaceContainer)
    assert 天气.title == '天气'

    历史天气 = 天气.children[3]
    assert isinstance(历史天气, MozPlaceContainer)
    assert 历史天气.title == '历史天气'
    assert len(历史天气.children) == 0

    newfolder = menu.children[len(menu.children)-1]
    assert isinstance(newfolder, MozPlaceContainer)
    assert isinstance(newfolder.title, str)
    assert 'newfolder' in newfolder.title.lower()
    tq1 = newfolder.children[0]
    tq2 = newfolder.children[1]
    assert isinstance(tq1, MozPlace)
    assert isinstance(tq2, MozPlace)
    assert '保定1月份天气' in tq1.title
    assert '北京历史气温' in tq2.title

    js1 = bms.root.toJSON()
    assert len(js1) > 0


def loadbms() -> firefoxbookmarks.Manager:
    s1 = os.getcwd()
    path1 = "z:/test/a.json"
    path2 = "tests/bookmarks-test.json"
    f = codecs.open(path2, "r", "utf-8")
    s = f.read()
    f.close()
    assert len(s) > 0
    bms = firefoxbookmarks.Manager()
    bms.Json2Bookmarks(s)
    return bms


# -----------
test_movefunc_without_folder()

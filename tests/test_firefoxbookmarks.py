import codecs
import json
import os
import firefoxbookmarks


def test_bookmark():
    bm = loadbms()
    bmroot = bm.root

    assert type(bmroot) == firefoxbookmarks.MozPlaceContainer
    assert isinstance(bmroot, firefoxbookmarks.MozPlaceContainer)
    assert bmroot.guid == "root________"

    children = bmroot.children
    assert len(children) > 0

    roots = ["menu________", "toolbar_____", "unfiled_____", "mobile______"]
    for i in range(len(children)):
        c1 = children[i]
        assert type(c1) == firefoxbookmarks.MozPlaceContainer
        assert isinstance(c1, firefoxbookmarks.MozPlaceContainer)
        assert c1.guid in roots
        assert c1.guid == roots[i]

    b1 = bmroot.children[0].children[0].children[2].children[0]
    assert isinstance(b1, firefoxbookmarks.MozPlace)
    assert b1.tags == ''
    assert b1.uri == 'https://finance.eastmoney.com/a/czqyw.html'

    bm.AddFolderToBookmark(bmroot.children[0], '')

    c1 = bmroot.children[0]
    assert isinstance(c1, firefoxbookmarks.MozPlaceContainer)
    assert c1.guid == roots[0]
    b1 = bmroot.children[0].children[0].children[2].children[0]
    assert isinstance(b1, firefoxbookmarks.MozPlace)
    assert b1.tags == 'News,财经'
    assert b1.uri == 'https://finance.eastmoney.com/a/czqyw.html'

    b2 = bmroot.children[0].children[1].children[3].children[0]
    assert b2.uri == 'https://lishi.tianqi.com/baoding/202001.html'
    assert '历史天气' in b2.tags


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


def test_MaxBookmarksId():
    bms = loadbms()
    maxid = bms.MaxBookmarksId()
    assert maxid == 36

    root = bms.root
    assert isinstance(root, firefoxbookmarks.MozPlaceContainer)
    assert root.guid == 'root________'
    children_len = len(root.children)
    children_max_index = root.MaxChildrenIndex()
    assert children_len == 4
    assert children_max_index == 4

    item = root.children[0]
    assert isinstance(item, firefoxbookmarks.MozPlaceContainer)
    assert item.title == 'menu'
    children_len = len(item.children)
    children_max_index = item.MaxChildrenIndex()
    assert children_len == 3
    assert children_max_index == 2

    item = item.children[0]
    assert isinstance(item, firefoxbookmarks.MozPlaceContainer)
    assert item.title.lower() == 'news'
    children_len = len(item.children)
    children_max_index = item.MaxChildrenIndex()
    assert children_len == 3
    assert children_max_index == 2


#----
test_MaxBookmarksId()

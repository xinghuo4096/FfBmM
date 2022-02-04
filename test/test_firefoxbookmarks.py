import os
import json
import codecs
from firefoxbookmarks.MozPlace import MozPlace
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer

from firefoxbookmarks.bookmark import AddFolderToBookmark, Json2Bookmarks


def test_bookmark():
    s1 = os.getcwd()
    path2 = "test/bookmarks-test.json"
    f = codecs.open(path2, "r", "utf-8")
    s = f.read()
    f.close()
    assert len(s) > 0

    bmroot = Json2Bookmarks(s)

    assert type(bmroot) == MozPlaceContainer
    assert isinstance(bmroot, MozPlaceContainer)
    assert bmroot.guid == "root________"

    children = bmroot.children
    assert len(children) > 0

    roots = ["menu________", "toolbar_____", "unfiled_____", "mobile______"]
    for i in range(len(children)):
        c1 = children[i]
        assert type(c1) == MozPlaceContainer
        assert isinstance(c1, MozPlaceContainer)
        assert c1.guid in roots
        assert c1.guid == roots[i]
    AddFolderToBookmark(bmroot.children[0], '')

    c1 = bmroot.children[0]
    assert isinstance(c1, MozPlaceContainer)
    assert c1.guid == roots[0]
    b1 = bmroot.children[0].children[0].children[2].children[0]
    assert isinstance(b1, MozPlace)
    assert b1.tags == 'News,财经'
    assert b1.uri == 'https://finance.eastmoney.com/a/czqyw.html'

    b2 = bmroot.children[0].children[1].children[3].children[0]
    assert b2.uri == 'https://lishi.tianqi.com/baoding/202001.html'
    assert '历史天气' in b2.tags


#----

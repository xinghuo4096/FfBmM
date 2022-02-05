import codecs
import json
import os
import time

from firefoxbookmarks.Manager import Manager
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer
from firefoxbookmarks.show import echar_ffbmtree

localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def test_showbm():
    s1 = os.getcwd()
    path1 = 'z:/test/a.json'
    path2 = "test/bookmarks-test.json"

    f = codecs.open(path2, "r", "utf-8")
    s = f.read()
    f.close()

    assert len(s) > 0
    bm = Manager()
    bm.Json2Bookmarks(s)
    bmroot = bm.root
    bm.AddFolderToBookmark(bmroot, '')

    assert type(bmroot) == MozPlaceContainer
    assert isinstance(bmroot, MozPlaceContainer)

    bmroot.value = 0
    bmroot.name = bmroot.root

    s2 = bmroot.toJSON()
    a1 = json.loads(s2)
    a2 = [a1]
    w = len(bm.folders) * 200
    h = len(bm.bookmarks) / len(bm.folders) * 200
    echar_ffbmtree(a2)


test_showbm()

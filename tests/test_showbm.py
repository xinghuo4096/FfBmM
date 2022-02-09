import codecs
import json
import os
import time
import firefoxbookmarks


localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def test_showbm():
    s1 = os.getcwd()
    path1 = 'z:/test/a.json'
    path2 = "tests/bookmarks-test.json"

    f = codecs.open(path2, "r", "utf-8")
    s = f.read()
    f.close()

    assert len(s) > 0
    bm = firefoxbookmarks.Manager()
    bm.Json2Bookmarks(s)
    bmroot = bm.root
    bm.AddTagsToBookmark(bmroot, '')

    assert type(bmroot) == firefoxbookmarks.MozPlaceContainer
    assert isinstance(bmroot,firefoxbookmarks.MozPlaceContainer)

    bmroot.value = 0
    bmroot.name = bmroot.root

    s2 = bmroot.toJSON()
    a1 = json.loads(s2)
    a2 = [a1]
    w = len(bm.folders) * 50
    h = len(bm.bookmarks) / len(bm.folders) * 450
    firefoxbookmarks.echar_ffbmtree(a2,10,w,h)


test_showbm()

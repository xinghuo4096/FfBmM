import codecs
import json
import os
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer
from firefoxbookmarks.bookmark import AddFolderToBookmark, BookMarks, Folders, Json2Bookmarks

from firefoxbookmarks.show import echar_ffbmtree
import time

localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def test_showbm():
    s1 = os.getcwd()
    path1 = 'z:/test/a.json'
    path2 = "test/bookmarks-test.json"

    f = codecs.open(path2, "r", "utf-8")
    s = f.read()
    f.close()
    assert len(s) > 0

    bmroot = Json2Bookmarks(s)
    assert type(bmroot) == MozPlaceContainer
    assert isinstance(bmroot, MozPlaceContainer)
    print(len(BookMarks))
    print(len(Folders))
    bmroot.value = 0
    bmroot.name = bmroot.root
    AddFolderToBookmark(bmroot, '')

    s2 = bmroot.toJSON()
    a1 = json.loads(s2)
    a2 = [a1]
    w = len(Folders) * 200
    h = len(BookMarks) / len(Folders) * 200
    echar_ffbmtree(a2)


test_showbm()
import os
import json
import codecs

from firefoxbookmarks.Bookmarks import BookMarks, Folders, BookmarksFacory, Json2Bookmarks, MozPlace, MozPlaceContainer


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


test_bookmark()
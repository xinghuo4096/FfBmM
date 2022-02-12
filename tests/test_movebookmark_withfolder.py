import codecs
import copy

from numpy import isin

from firefoxbookmarks import MozPlace, MozPlaceContainer
from firefoxbookmarks import Manager
import firefoxbookmarks
from firefoxbookmarks.MozBaseItem import MozBaseItem
from firefoxbookmarks.new_folder import new_folder


def test_move_bookmark_with_foler():
    bms = loadbms()
    bms_copy = copy.deepcopy(bms)
    maxid = bms_copy.get_maxid()

    find = 'baidu'
    delitem = [bm for bm in bms.bookmarks if func(find, bm)]
    for item in delitem:
        parent = [folder for folder in bms.folders if folder.guid ==
                  bms.tree.get(item.guid)]
        pitem = parent[0]
        assert isinstance(pitem, MozPlaceContainer)
        pitem.DelChildern(item)
# bms_copy
    delitem = [bm for bm in bms_copy.bookmarks if not func(find, bm)]
    for item in delitem:
        parent = [folder for folder in bms_copy.folders if folder.guid ==
                  bms_copy.tree.get(item.guid)]
        pitem = parent[0]
        assert isinstance(pitem, MozPlaceContainer)
        pitem.DelChildern(item)

    for folder in bms_copy.folders+bms_copy.separators:
        maxid += 1
        folder.id = maxid
        assert isinstance(folder, MozBaseItem)

        if folder.guid in bms_copy.ROOTS_GUID:
            folder.title = folder.root

        folder.root = ''
        folder.guid = firefoxbookmarks.getguid(folder.title)

    menu = bms.root.children[0]
    assert isinstance(menu, MozPlaceContainer)
    menu.AddChildern(bms_copy.root)

    bms2 = copy.deepcopy(bms)
    js1 = bms2.root.toJSON()
    bms2.Json2Bookmarks(js1)
    bms2.traversal(bms2.root)

    for item in bms2.folders:
        assert isinstance(item, MozPlaceContainer)
        if len(item.children) == 0:
            parent = [folder for folder in bms2.folders if folder.guid ==
                      bms2.tree.get(item.guid)]
            pitem = parent[0]
            assert isinstance(pitem, MozPlaceContainer)
            pitem.DelChildern(item)

    js1 = bms2.root.toJSON()
    assert len(js1) > 0

    path1 = "outdata/new-bookmarks-test.json"
    f = codecs.open(path1, "w", "utf-8")
    s = f.write(js1)
    f.close()


def func(findstr: str, item: MozPlace):
    return findstr in item.uri


def loadbms() -> Manager:
    path1 = "z:/test/a.json"
    path2 = "tests/bookmarks-test.json"
    f = codecs.open(path2, "r", "utf-8")
    s = f.read()
    f.close()
    assert len(s) > 0
    bms = Manager()
    bms.Json2Bookmarks(s)
    bms.AddTagsToBookmark(bms.root, '')
    bms.traversal(bms.root)
    return bms


# ----
def main():
    test_move_bookmark_with_foler()


if __name__ == '__main__':
    main()

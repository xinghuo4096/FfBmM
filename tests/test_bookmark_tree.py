import codecs
from firefoxbookmarks import Manager


def test_bookmark_traversal():
    bms = loadbms()
    bms.traversal(bms.root)
    assert bms.tree
    for item in bms.tree:
        bm = [bm for bm in bms.bookmarks if bm.guid == item]
        if bm:
            folder = [f for f in bms.folders if f.guid == bms.tree.get(item)]
        else:
            folder = [f for f in bms.folders if f.guid == item]
        assert  folder

    bm = []
    assert not bm
    bm = [bm for bm in bms.tree if bm == 'qWqX1EzEZAMf']
    assert bm
    assert bm[0]

    bm = [bm for bm in bms.bookmarks if bm.guid == 'qWqX1EzEZAMf']
    assert bm[0].uri == 'https://news.sina.com.cn/'

    folder = [f for f in bms.folders if f.guid == bms.tree.get(bm[0].guid)]
    assert folder[0].title.lower() == 'news'


def test_root2node():
    bms = loadbms()
    bms.traversal(bms.root)
    bm = [bm for bm in bms.bookmarks if bm.guid == 'qWqX1EzEZAMf']
    assert bm[0].uri == 'https://news.sina.com.cn/'

    a = bms.get_root2node(bm[0])
    assert a
    assert a[0].lower() == 'news'
    assert a[1].lower() == 'menu'


def loadbms() -> Manager:
    path2 = "tests/bookmarks-test.json"
    f = codecs.open(path2, "r", "utf-8")
    s = f.read()
    f.close()
    assert len(s) > 0
    bms = Manager()
    bms.Json2Bookmarks(s)
    return bms

# ----


def main():
    test_root2node()


if __name__ == '__main__':
    main()

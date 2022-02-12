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
    assert bm[0].tags=='News'

    bm = [bm for bm in bms.bookmarks if bm.guid == 'NnP7Tc0XymNJ']
    assert '.eastmoney.com' in bm[0].uri
    assert bm[0].tags=='News,财经'

    root2node = bms.get_root2node(bm[0])
    assert root2node
    assert len(root2node)==4
    assert root2node[0].lower() == bms.ROOTS_ROOT[0].lower()
    assert root2node[1].lower() == bms.ROOTS_ROOT[1].lower()
    assert root2node[2].lower() == 'news'
    assert root2node[3].lower() == '财经'


def loadbms() -> Manager:
    path1='z:/test/a.json'
    path2 = "tests/bookmarks-test.json"
    f = codecs.open(path2, "r", "utf-8")
    s = f.read()
    f.close()
    assert len(s) > 0
    bms = Manager()
    bms.Json2Bookmarks(s)
    bms.AddTagsToBookmark(bms.root,'')
    return bms

# ----


def main():
    test_root2node()


if __name__ == '__main__':
    main()

import codecs
import json
import os
import firefoxbookmarks


def bmfindFunc(self: firefoxbookmarks.MozPlace, data: str):
    return (data in self.title)


def test_bmfind():
    bm = loadbms()
    bmroot = bm.root
    b1 = bmroot.children[0].children[0].children[2].children[0]
    assert isinstance(b1, firefoxbookmarks.MozPlace)
    assert b1.tags == ''
    assert b1.uri == 'https://finance.eastmoney.com/a/czqyw.html'

    assert not b1.findByUri('baidu')
    assert not b1.findByUri('Finance.eastmoney.com')
    assert b1.findByUri('eastmoney')
    assert b1.findByUri('finance')
    assert b1.findByUri('finance.eastmoney.com')
    assert not b1.findByUri('')
  
    assert not b1.find('百度',bmfindFunc)
    assert b1.find('东方财富网',bmfindFunc)

def test_LoadBookmark():
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

    bm.AddTagsToBookmark(bmroot.children[0], '')

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


# ----
def main():
    test_LoadBookmark()
    
if __name__ == '__main__':
    main()


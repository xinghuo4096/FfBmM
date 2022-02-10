import codecs

import os
import firefoxbookmarks
from firefoxbookmarks.MozBaseItem import MozBaseItem
from firefoxbookmarks.MozPlace import MozPlace
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer

def test_movebm():
    bms=loadbms()
    root=bms.root
    bms.AddTagsToBookmark(root,'')
    folder=bms.move_bookmarks_to_newfolder('baidu')
    assert folder
    
    assert isinstance(folder,MozPlaceContainer)
    bd=folder.children[0]
    assert isinstance(bd,MozPlace)
    assert bd.uri=='http://news.baidu.com/'
    assert 'news' in  bd.tags.lower()
    print(bd.tags.lower())
    assert '百度新闻' in bd.title
    
    


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
#-----------
test_movebm()

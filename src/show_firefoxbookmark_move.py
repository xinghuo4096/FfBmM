import codecs
from firefoxbookmarks.Manager import Manager

def main():
    bms = load_bms()
    bms.AddTagsToBookmark(bms.root,'')
    bms.move_bookmarks_to_newfolder('rrys2020.com')    
    save_json(bms)
    return bms


def load_bms():
    path1 = "z:/test/a.json"
    path2 = "tests/bookmarks-test.json"
    f = codecs.open(path1, "r", "utf-8")
    s = f.read()
    f.close()
    assert len(s) > 0
    bms = Manager()
    bms.Json2Bookmarks(s)
    return bms



def save_json(bms):
    js1 = bms.root.toJSON()
    assert len(js1) > 0

    path1 = "outdata/new-bookmarks-test.json"
    f = codecs.open(path1, "w", "utf-8")
    s = f.write(js1)
    f.close()


# -----------------------
if __name__ == '__main__':
    main()

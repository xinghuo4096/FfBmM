import datetime
import time
import json
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer
from firefoxbookmarks.new_bookmarks_folder import getguid


def test_newuuid():
    name = "test"
    str1 = getguid(name)
    assert len(str1) > 0
    assert len(str1) == 12


def test_newfolder():

    a = float('1643120121073000') / (pow(10, 6))
    t = time.localtime(a)
    print(time.strftime("%Y-%m-%d %H:%M:%S", t))

    dt = datetime.datetime.fromtimestamp(a)
    print(dt.strftime("%Y-%m-%d %H:%M:%S.%f"))
    sdt = str(int(dt.timestamp() * pow(10, 6)))

    folder = "newFolder"
    folder = MozPlaceContainer(getguid(folder), folder, 0, sdt, sdt, 1, 2,
                               'text/x-moz-place-container', '', [])
    assert len(folder.guid) > 0
    assert len(folder.guid) == 12
    assert folder.date_added == '1643120121073000'
    assert folder.last_modified == '1643120121073000'


#--------------

test_newfolder()
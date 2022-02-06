import datetime
import time
import os
import sys
a=os.getcwd()
b=os.getenv('pythonpath')
c=sys.path
import firefoxbookmarks



def test_newuuid():
    name = "test"
    str1 =firefoxbookmarks.getguid(name)
    assert len(str1) > 0
    assert len(str1) == 12


def test_newfolder():

    a = float('1643120121073000') / (pow(10, 6))
    t = time.localtime(a)
    s1 = time.strftime("%Y-%m-%d %H:%M:%S", t)
    assert s1 == '2022-01-25 22:15:21'

    dt = datetime.datetime.fromtimestamp(a)
    s1 = dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    assert s1 == '2022-01-25 22:15:21.073000'

    name = "newFolder"
    folder = firefoxbookmarks.newfolder(name, 1, 2)
    assert isinstance(folder,firefoxbookmarks.MozPlaceContainer)
    assert isinstance(folder, firefoxbookmarks.MozBaseItem)
    assert len(folder.guid) > 0
    assert len(folder.guid) == 12
    assert len(folder.date_added) == 16
    assert len(folder.last_modified) == 16


#--------------

test_newuuid()
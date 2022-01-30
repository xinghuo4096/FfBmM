import codecs
import json
import os

from firefoxbookmarks.Bookmarks import Json2Bookmarks, MozPlaceContainer
from firefoxbookmarks.showbookmarks import echar_ffbmtree
import time

localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
data1 = {
    "children": [
        {
            "name": "github",
            "value": 1,
            "title": "github交朋友",
            "uri": "www.github.com",
            "site": "github.com"
        },
        {
            "children": [{
                "children": [{
                    "name": "百度",
                    "title": localtime,
                    "uri": "www.baidu.com",
                    "site": "baidu.com"
                }],
                "name":
                "E"
            }, {
                "name": "F",
                "value": localtime
            }],
            "name":
            "C",
        },
        {
            "children": [
                {
                    "children": [{
                        "name": "J"
                    }, {
                        "name": "K"
                    }],
                    "name": "G"
                },
                {
                    "name": "H"
                },
            ],
            "name":
            "D",
        },
    ],
    "name":
    "天气网",
    "title":
    "天气网有天气",
    "uri":
    "http://www.weather.com.cn/",
    "site":
    "weather.com.cn",
    "value":
    "http://www.weather.com.cn/"
}
testdata = [data1]


def test_show():
    s1 = os.getcwd()
    path2 = "test/bookmarks-test.json"
    f = codecs.open(path2, "r", "utf-8")
    s = f.read()
    f.close()
    assert len(s) > 0

    bmroot = Json2Bookmarks(s)
    assert type(bmroot) == MozPlaceContainer
    assert isinstance(bmroot, MozPlaceContainer)

    bmroot.value = 0

    s2 = bmroot.toJSON()
    a1 = json.loads(s2)
    a2 = [a1]
    print(type(data1))
    print(type(a1))
    echar_ffbmtree(a2)


test_show()
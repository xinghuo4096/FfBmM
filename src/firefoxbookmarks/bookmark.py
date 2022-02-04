from ast import keyword
from ctypes.wintypes import tagSIZE
from inspect import TPFLAGS_IS_ABSTRACT
import os
import json
import codecs
from urllib.parse import urlparse

from firefoxbookmarks.MozPlace import MozPlace
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer
from firefoxbookmarks.MozSeparator import MozSeparator

BookMarks = []
Folders = []
BookMarksRoot = object
NewBookMarksRoot = object
ROOTSGUID = ["menu________", "toolbar_____", "unfiled_____", "mobile______"]


def Json2Bookmarks(s):
    root = json.loads(s, object_hook=BookmarksFacory)
    BookMarksRoot = root
    return root


def BookmarksFacory(d):
    t1 = d['type']
    if t1 == "text/x-moz-place":
        ret = MozPlace.dict2MozPlace(d)
        BookMarks.append(ret)
    else:
        if t1 == 'text/x-moz-place-container':
            ret = MozPlaceContainer.dict2MozPlaceContainer(d)
            Folders.append(ret)
        else:
            if t1 == "text/x-moz-place-separator":
                ret = MozSeparator.dict2mozeparator(d)
            else:
                raise "unkonw type:" + t1
    return ret


def AddFolderToBookmark(bmobj, nowfolder):

    if type(bmobj) == MozPlace:
        assert isinstance(bmobj, MozPlace)
        if nowfolder not in bmobj.tags:
            if (bmobj.tags == ''):
                bmobj.tags = nowfolder
            else:
                bmobj.tags = bmobj.tags + ',' + nowfolder
    else:
        if type(bmobj) == MozPlaceContainer:
            assert isinstance(bmobj, MozPlaceContainer)

            if (bmobj.guid not in ROOTSGUID) and (bmobj.title
                                                  not in nowfolder):
                if nowfolder == '':
                    nowfolder = bmobj.title
                else:
                    nowfolder = nowfolder + ',' + bmobj.title
            for obj in bmobj.children:
                AddFolderToBookmark(obj, nowfolder)
        else:
            if type(bmobj) == MozSeparator:
                pass
            else:
                raise "unkonw type:" + type(bmobj)


#------------------------


def main():
    pass


if __name__ == '__main__':
    main()
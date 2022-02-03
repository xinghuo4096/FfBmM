from ast import keyword
from ctypes.wintypes import tagSIZE
from inspect import TPFLAGS_IS_ABSTRACT
import os
import json
import codecs
from urllib.parse import urlparse

BookMarks = []
Folders = []
BookMarksRoot = object
NewBookMarksRoot = object
ROOTSGUID = ["menu________", "toolbar_____", "unfiled_____", "mobile______"]


class MozBaseItem(object):

    def __init__(self, guid, title, index, dateAddedid, lastModified, id,
                 typeCode, type):
        self.guid = guid
        self.title = title
        self.index = index
        self.date_added = dateAddedid
        self.last_modified = lastModified
        self.id = id
        self.type_code = typeCode
        self.type = type
        if len(title) > 16:
            self.name = title[0:16] + ".."
        else:
            self.name = title

        self.value = guid

    def dict2mozBaseItem(d):
        return MozBaseItem(d['guid'], d['title'], d['index'], d['dateAdded'],
                           d['lastModified'], d['id'], d['typeCode'],
                           d['type'])

    def toJSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=0)


class MozPlaceContainer(MozBaseItem):

    def __init__(self, guid, title, index, dateAddedid, lastModified, id,
                 typeCode, type, root, children):
        super().__init__(guid, title, index, dateAddedid, lastModified, id,
                         typeCode, type)
        self.root = root
        self.children = children
        if self.title is not None:
            self.name = self.title
        if self.root is not None and root != '':
            self.name = root

    def dict2MozPlaceContainer(d):

        a1 = d.get('root', '')
        a2 = d.get('children', [])
        return MozPlaceContainer(d['guid'], d['title'], d['index'],
                                 d['dateAdded'], d['lastModified'], d['id'],
                                 d['typeCode'], d['type'], d.get('root', ''),
                                 d.get('children', []))


class MozPlace(MozBaseItem):

    def __init__(self, guid, title, index, dateAddedid, lastModified, id,
                 typeCode, type, uri, iconuri, tags, keyword, postData):
        super().__init__(guid, title, index, dateAddedid, lastModified, id,
                         typeCode, type)
        self.iconuri = iconuri
        self.uri = uri
        self.tags = tags
        self.keyword = keyword
        self.post_data = postData

        if len(self.name) < 1 and len(self.uri) > 1:
            self.name = urlparse(uri).hostname

    def dict2MozPlace(d):
        return MozPlace(
            d['guid'],
            d['title'],
            d['index'],
            d['dateAdded'],
            d['lastModified'],
            d['id'],
            d['typeCode'],
            d['type'],
            d['uri'],
            d.get('iconuri', ''),
            d.get('tags', ''),
            d.get('keyword', ''),
            d.get('postData', ''),
        )


class MozSeparator(MozBaseItem):

    def __init__(self, guid, title, index, dateAddedid, lastModified, id,
                 typeCode, type):
        super().__init__(guid, title, index, dateAddedid, lastModified, id,
                         typeCode, type)
        self.name = '|'
        self.title = 'Separator'

    def dict2mozeparator(d):
        return MozSeparator(d['guid'], d['title'], d['index'], d['dateAdded'],
                            d['lastModified'], d['id'], d['typeCode'],
                            d['type'])


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
                print(nowfolder)
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
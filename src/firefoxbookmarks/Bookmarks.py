from ast import keyword
from ctypes.wintypes import tagSIZE
from inspect import TPFLAGS_IS_ABSTRACT
import os
import json
import codecs

BookMarks = []
Folders = []


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

    def dict2mozBaseItem(d):
        return MozBaseItem(d['guid'], d['title'], d['index'], d['dateAdded'],
                           d['lastModified'], d['id'], d['typeCode'],
                           d['type'])


class MozPlaceContainer(MozBaseItem):

    def __init__(self, guid, title, index, dateAddedid, lastModified, id,
                 typeCode, type, root, children):
        super().__init__(guid, title, index, dateAddedid, lastModified, id,
                         typeCode, type)
        self.root = root
        self.children = children

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
            d.get('iconuri', ''),
            d['uri'],
            d.get('tags', ''),
            d.get('keyword', ''),
            d.get('postData', ''),
        )


class MozSeparator(MozBaseItem):

    def __init__(self, guid, title, index, dateAddedid, lastModified, id,
                 typeCode, type):
        super().__init__(guid, title, index, dateAddedid, lastModified, id,
                         typeCode, type)

    def dict2mozeparator(d):
        return MozSeparator(d['guid'], d['title'], d['index'], d['dateAdded'],
                            d['lastModified'], d['id'], d['typeCode'],
                            d['type'])


def Json2Bookmarks(s):
    root = json.loads(s, object_hook=BookmarksFacory)
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


#------------------------


def main():
    pass


if __name__ == '__main__':
    main()
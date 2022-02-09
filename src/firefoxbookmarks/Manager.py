import json

from firefoxbookmarks.MozBaseItem import MozBaseItem
from firefoxbookmarks.MozPlace import MozPlace
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer
from firefoxbookmarks.MozSeparator import MozSeparator

class Manager(object):
    """docstring for Manager."""
    ROOTSGUID = [
        "menu________", "toolbar_____", "unfiled_____", "mobile______"
    ]

    def __init__(self):
        self.bookmarks = []
        self.folders = []
        self.separators = []
        self.maxid = -1
        self.root = []

    def MaxBookmarksId(self):
        maxid = 0
        for item in self.folders:
            if int(item.id) > maxid:
                maxid = int(item.id)
        for item in self.bookmarks:
            if int(item.id) > maxid:
                maxid = int(item.id)
        for item in self.separators:
            if int(item.id) > maxid:
                maxid = int(item.id)
        self.maxid = maxid
        return maxid

    def BookmarksFacory(self, data) -> MozBaseItem:
        t1 = data['type']
        if t1 == "text/x-moz-place":
            ret = MozPlace.dict2MozPlace(data)
            self.bookmarks.append(ret)
        else:
            if t1 == 'text/x-moz-place-container':
                ret = MozPlaceContainer.dict2MozPlaceContainer(data)
                self.folders.append(ret)
            else:
                if t1 == "text/x-moz-place-separator":
                    ret = MozSeparator.dict2mozeparator(data)
                    self.separators.append(ret)
                else:
                    raise "unkonw type:" + t1
        return ret

    def Json2Bookmarks(self, s):
        root = json.loads(s, object_hook=self.BookmarksFacory)
        self.root = root
        return self.root

    def Bookmarks2Json(self, s):
        root = json.dumps(self,)  
        self.root = root
        return self.root
    def AddTagsToBookmark(self, bmobj, nowfolder):

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

                if (bmobj.guid
                        not in Manager.ROOTSGUID) and (bmobj.title
                                                       not in nowfolder):
                    if nowfolder == '':
                        nowfolder = bmobj.title
                    else:
                        nowfolder = nowfolder + ',' + bmobj.title
                for obj in bmobj.children:
                    self.AddTagsToBookmark(obj, nowfolder)
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

import copy
import json
from multiprocessing import managers
import time

from numpy import isin
from firefoxbookmarks.MozBaseItem import MozBaseItem
from firefoxbookmarks.MozPlace import MozPlace
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer
from firefoxbookmarks.MozSeparator import MozSeparator
from firefoxbookmarks.new_folder import new_folder


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

    def move_bookmark_digui(self,parent: MozPlaceContainer, findstr, folder: MozPlaceContainer, findfunc=MozPlace.findByUri):
        parent_copy = copy.deepcopy(parent)
        assert isinstance(parent_copy, MozPlaceContainer)
        for item_copy in parent_copy.children:
            item = parent.find_item(item_copy)
            if isinstance(item_copy, MozPlace):
                if item_copy.findByUri(findstr):
                    folder.AddChildern(item)
                    parent.DelChildern(item)

            else:
                if isinstance(item, MozPlaceContainer):                    
                   self.move_bookmark_digui(item, findstr, folder, findfunc)
                else:
                    pass

    def move_bookmarks_to_newfolder(self, findstr, newfoldname="NewFolder-"+str(time.ctime()), from_rootname='menu', func=MozPlace.find) -> MozPlaceContainer:
        from_root = self.root
        if from_rootname == 'menu':
            from_root = self.root.children[0]
            assert isinstance(from_root, MozPlaceContainer)
            assert from_root.title == 'menu'
        assert isinstance(findstr, str)

        maxid = self.MaxBookmarksId()
        maxid += 1
        folder = new_folder(newfoldname, 1, maxid)
        self.move_bookmark_digui(from_root, findstr, folder)

        from_root.AddChildern(folder)
        return self.root

# ------------------------


def main():
    pass


if __name__ == '__main__':
    main()

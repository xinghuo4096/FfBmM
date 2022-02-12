import codecs
import json
import time
from firefoxbookmarks.MozBaseItem import MozBaseItem
from firefoxbookmarks.MozPlace import MozPlace
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer
from firefoxbookmarks.MozSeparator import MozSeparator
from firefoxbookmarks.new_folder import new_folder
from firefoxbookmarks.move_folder import move_bookmark_with_folder, move_bookmark_without_folder


# TODO 修改readme
# TODO 删除list和for联合时，经验
# for item in parent.Childern:
#    parent.Childern.remove(item)


class Manager(object):
    """docstring for Manager."""
    PLACEROOT = 'root________'
    ROOTS_GUID = [
        "root________", "menu________", "toolbar_____", "unfiled_____", "mobile______"
    ]
    ROOTS_ROOT = [
        "placesRoot", "bookmarksMenuFolder", "toolbarFolder", "unfiledBookmarksFolder", "mobileFolder"
    ]

    def __init__(self):
        self.bookmarks = []
        self.folders = []
        self.separators = []

        self.maxid = -1
        self.root = []
        self.tree = dict()

    def get_maxid(self):
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
                ret = MozPlaceContainer.dict2MozPlaceContainer(
                    data)
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

    def traversal(self, parent: MozPlaceContainer):
        for item in parent.children:
            if isinstance(item, MozPlace):
                self.tree.update({item.guid: parent.guid})
            else:
                if isinstance(item, MozPlaceContainer):
                    self.tree.update({item.guid: parent.guid})
                    self.traversal(item)
                else:
                    if isinstance(item, MozSeparator):
                        pass
                    else:
                        raise Exception('unkonw type:'+item.guid)

    def find_treenode(self, guid: str):
        item = [b for b in self.bookmarks if b.guid == guid]
        if not item:
            item = [f for f in self.folders if f.guid == guid]
        return item

    def get_root2node(self, item: MozBaseItem) -> list:
        parent = [folder for folder in self.folders if folder.guid ==
                  self.tree.get(item.guid, None)]
        root2node = list()
        while parent:
            find = parent[0]
            if find.guid in self.ROOTS_GUID:
                root2node.append(find.root)
            else:
                if find.title:
                    root2node.append(find.title)
                else:
                    pass
            parent = [folder for folder in self.folders if folder.guid ==
                      self.tree.get(find.guid, None)]
        root2node = root2node[::-1]
        return root2node

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
                        not in Manager.ROOTS_GUID) and (bmobj.title
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

    def movefunc_without_folder(self, findstr, newfoldname="NewFolder-"+str(time.ctime()), from_rootname='menu', func=MozPlace.find) -> MozPlaceContainer:
        from_root = self.root
        if from_rootname == 'menu':
            from_root = self.root.children[0]
            assert isinstance(from_root, MozPlaceContainer)
            assert from_root.title == 'menu'
        assert isinstance(findstr, str)

        maxid = self.get_maxid()
        maxid += 1
        folder = new_folder(newfoldname, 1, maxid)
        move_bookmark_without_folder(
            from_root, findstr, folder)

        from_root.AddChildern(folder)
        return self.root

    def movefunc_with_folder(self, findstr, newfoldname="NewFolder-"+str(time.ctime()), from_rootname='menu', func=MozPlace.find):
        return move_bookmark_with_folder(
            self, findstr, newfoldname, from_rootname, func)

    def save_firefoxbookmarksjson(self, outfile='outdata/new-bookmarks-test.json'):
        js1 = self.root.toJSON()
        assert len(js1) > 0

        path1 = outfile
        f = codecs.open(path1, "w", "utf-8")
        s = f.write(js1)
        f.close()

    def loadbms(self, source='tests/bookmarks-test.json'):
        f = codecs.open(source, "r", "utf-8")
        s = f.read()
        f.close()
        assert len(s) > 0
        self.Json2Bookmarks(s)
        self.AddTagsToBookmark(self.root, '')
        self.traversal(self.root)
        return self
# ------------------------


def main():
    pass


if __name__ == '__main__':
    main()

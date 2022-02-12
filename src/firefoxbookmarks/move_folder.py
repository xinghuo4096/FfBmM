import copy

from firefoxbookmarks.MozBaseItem import MozBaseItem
from firefoxbookmarks.MozPlace import MozPlace
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer
from firefoxbookmarks.new_folder import getguid, new_folder


# TODO 和manager数据耦合问题。本次版本不修改。
def move_bookmark_with_folder(bms, findstr: str, newfoldname, from_rootname, find_func=MozPlace.find):

    from firefoxbookmarks.Manager import Manager

    assert isinstance(bms, Manager)
    bms_copy = copy.deepcopy(bms)
    maxid = bms_copy.get_maxid()

    delitem = [bm for bm in bms.bookmarks if find_func(bm, findstr)]
    for item in delitem:
        parent = [folder for folder in bms.folders if folder.guid ==
                  bms.tree.get(item.guid)]
        pitem = parent[0]
        assert isinstance(pitem, MozPlaceContainer)
        pitem.DelChildern(item)
# bms_copy
    delitem = [
        bm for bm in bms_copy.bookmarks if not find_func(bm, findstr)]
    for item in delitem:
        parent = [folder for folder in bms_copy.folders if folder.guid ==
                  bms_copy.tree.get(item.guid)]
        pitem = parent[0]
        assert isinstance(pitem, MozPlaceContainer)
        pitem.DelChildern(item)

    for folder in bms_copy.folders+bms_copy.separators:
        maxid += 1
        folder.id = maxid
        assert isinstance(folder, MozBaseItem)

        if folder.guid in bms_copy.ROOTS_GUID:
            folder.title = folder.root

        folder.root = ''
        folder.guid = getguid(folder.title)

    menu = bms.root.children[0]
    assert isinstance(menu, MozPlaceContainer)
    bms_copy.root.title = newfoldname
    menu.AddChildern(bms_copy.root)

    bms2 = remove_emtpyfolder(bms)

    return bms2


def remove_emtpyfolder(bms):
    bms2 = copy.deepcopy(bms)
    js1 = bms2.root.toJSON()
    bms2.Json2Bookmarks(js1)
    bms2.traversal(bms2.root)

    for item in bms2.folders:
        assert isinstance(item, MozPlaceContainer)
        if len(item.children) == 0:
            parent = [folder for folder in bms2.folders if folder.guid ==
                      bms2.tree.get(item.guid)]
            pitem = parent[0]
            assert isinstance(pitem, MozPlaceContainer)
            pitem.DelChildern(item)
    return bms2


def move_bookmark_without_folder(parent: MozPlaceContainer, findstr, folder: MozPlaceContainer, findfunc=MozPlace.findByUri):
    parent_copy = copy.deepcopy(parent)
    assert isinstance(parent_copy, MozPlaceContainer)
    for item_copy in parent_copy.children:
        item = parent.find_byguid(item_copy)
        if isinstance(item_copy, MozPlace):
            if item_copy.findByUri(findstr):
                folder.AddChildern(item)
                parent.DelChildern(item)

        else:
            if isinstance(item, MozPlaceContainer):
                move_bookmark_without_folder(item, findstr, folder, findfunc)
            else:
                pass

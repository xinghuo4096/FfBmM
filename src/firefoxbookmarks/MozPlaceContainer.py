from firefoxbookmarks.MozBaseItem import MozBaseItem


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
        return MozPlaceContainer(d['guid'], d.get('title',''), d['index'],
                                 d['dateAdded'], d['lastModified'], d['id'],
                                 d['typeCode'], d['type'], d.get('root', ''),
                                 d.get('children', []))

    def MaxChildrenIndex(self) -> int:
        ret = -1
        for item in self.children:
            assert isinstance(item, MozBaseItem)
            if int(item.index) > ret:
                ret = int(item.index)
        return ret

    def AddChildern(self, c):
        assert isinstance(self.children, list)
        assert isinstance(c, MozBaseItem)
        c.index = self.MaxChildrenIndex()+1
        self.children.append(c)

    def DelChildern(self, c):
        assert isinstance(self.children, list)
        assert isinstance(c, MozBaseItem)
        for x in self.children:
            assert isinstance(x, MozBaseItem)
            if x.guid == c.guid:
                self.children.remove(x)

    def find_byguid(self, c):
        assert isinstance(self.children, list)
        assert isinstance(c, MozBaseItem)
        ret = None
        for x in self.children:
            assert isinstance(x, MozBaseItem)
            if x.guid == c.guid:
                ret = x
        return ret

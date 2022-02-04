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
        return MozPlaceContainer(d['guid'], d['title'], d['index'],
                                 d['dateAdded'], d['lastModified'], d['id'],
                                 d['typeCode'], d['type'], d.get('root', ''),
                                 d.get('children', []))
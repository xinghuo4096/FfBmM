from  firefoxbookmarks.MozBaseItem import MozBaseItem
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
from urllib.parse import urlparse

from  firefoxbookmarks.MozBaseItem import MozBaseItem


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

import json


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

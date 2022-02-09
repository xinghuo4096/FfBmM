import json
from types import NoneType


class MozBaseItem(object):

    def __init__(self, guid, title, index, dateAdded, lastModified, id,
                 typeCode, type):
        self.guid = guid
        self.title = title
        self.index = index
        self.dateAdded = dateAdded
        self.lastModified = lastModified
        self.id = id
        self.typeCode = typeCode
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
    def isempty(self,x):
        
        assert isinstance(x,tuple)
        data=x[1]
        
        if isinstance(data,(str,list)):            
            return len(data)>0
        else:
            if isinstance(data,int):
                return True
            else:
             if isinstance(data,NoneType):
                 return False
             else:
                print(type(x[1])) 
                print(x)
                raise Exception ("json type error !")
        return True

    def ggg(self,x):
        assert isinstance(x,object)       
        d1=x.__dict__      
        c=dict(filter(self.isempty, d1.items()))
        return c

    def toJSON(self):
        return json.dumps(self,
                          default=self.ggg,
                          sort_keys=False,ensure_ascii=False,
                          indent='\t')


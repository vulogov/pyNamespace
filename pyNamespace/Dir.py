from .Object import Object

class Dir(Object):
    def __init__(self, ns, name, **kw):
        Object.__init__(self, ns, name, **kw)
    def isDir(self):
        return True
    def isObject(self):
        return False

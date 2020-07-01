import time
import uuid
class Object:
    def __init__(self, ns, name, value=None, **kw):
        self.ns = ns
        self.name = name
        for k in kw:
            setattr(self, k, kw[k])
        self.stamp = time.time()
        self.reinit()
        if value is not None:
            self.value = value
    def reinit(self):
        self.id = str(uuid.uuid4())
    def isDir(self):
        return False
    def isObject(self):
        return True
    @property
    def value(self):
        if hasattr(self, '_value') is True:
            return self._value
        return self
    @value.setter
    def value(self, val):
        self._value = val
    def map(self, f=None):
        if callable(f) is True:
            return f(self)
        return self
    def __call__(self, *args, **kw):
        if hasattr(self, "_value") is True and callable(self._value) is True:
            self._value(*args, **kw)
        return None
    def __repr__(self):
        _repr = "Object(%s) = %s"%(self.id, self.name)
        return _repr

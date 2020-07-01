import os
import os.path
import graph
from .Dir import Dir
from .Object import Object

class Namespace:
    def __init__(self, *derive):
        self.value = graph.Graph()
        for d in derive:
            if isinstance(d, dict) is True:
                self.value.from_dict(d)
            if isinstance(d, list) is True:
                self.value.from_list(d)
            if insinstance(d, graph.Graph) is True:
                self.value.from_dict(d.to_dict())
        if "/" not in self.value:
            self.value.add_node("/", Dir(self, "", fullpath=""))
    def _mkdir(self, current, p, fp):
        if len(p) == 0:
            return current
        if p[0] == '':
            return self._mkdir(current, p[1:], fp)
        n = self.value.nodes(from_node=current.id)
        fp.append(p[0])
        for _name in n:
            _n = self.value.node(_name)
            if _n.name == p[0]:
                return self._mkdir(_n, p[1:], fp)
        d = Dir(self, p[0], fullpath="/".join(fp))
        self.value.add_node(d.id, d)
        self.value.add_edge(current.id, d.id)
        return self._mkdir(d, p[1:], fp)
    def mkdir(self, path):
        path = os.path.normpath(path)
        root = self.value.node("/")
        p = path.split("/")
        return self._mkdir(root, p, [])
    def set(self, path, value):
        path = os.path.normpath(path)
        dir = os.path.dirname(path)
        name = os.path.basename(path)
        ld = self.mkdir(dir)
        for _name in self.value.nodes(from_node=ld.id):
            _n = self.value.node(_name)
            if _n.name == name:
                _n.value = value
                return _n
        o = Object(self, name, value, fullpath=path)
        self.value.add_node(o.id, o)
        self.value.add_edge(ld.id, o.id)
        return o
    def object(self, path, default=None):
        path = os.path.normpath(path)
        dir = os.path.dirname(path)
        name = os.path.basename(path)
        ld = self.mkdir(dir)
        for _name in self.value.nodes(from_node=ld.id):
            _n = self.value.node(_name)
            if _n is None:
                continue
            if _n.name == name:
                if hasattr(_n, "srcpath") is True:
                    return self.object(_n.srcpath, default)
                return _n
        return default
    def get(self, path, default=None):
        o = self.object(path, default)
        if o is None:
            return default
        return o.value
    def rm(self, path):
        o = self.get(path, None)
        if o is None:
            return False
        for _from, _to, _weight in self.value.edges(to_node=o.id):
            self.value.del_edge(_from, _to)
        for _from, _to, _weight in self.value.edges(from_node=o.id):
            self.value.del_edge(_from, _to)
        self.value.del_node(o.id)
        self.__purge_nodes()
        return True
    def link(self, src_path, dst_path):
        dst_path = os.path.normpath(dst_path)
        src_path = os.path.normpath(src_path)
        src = self.object(src_path, None)
        if src is None:
            return False
        dst = self.object(dst_path, None)
        if dst is not None:
            return False
        dst_name = os.path.basename(dst_path)
        dst_path = os.path.dirname(dst_path)
        dst_dir = self.mkdir(dst_path)
        o = Object(self, dst_name, None, fullpath=dst_path, srcpath=src_path)
        self.value.add_node(o.id, o)
        self.value.add_edge(dst_dir.id, o.id)
        return True
    def ref(self, src_path, dst_path):
        dst_path = os.path.normpath(dst_path)
        src_path = os.path.normpath(src_path)
        src = self.object(src_path)
        if src is None:
            return False
        dst = self.object(dst_path)
        if dst is None:
            dst = self.mkdir(dst_path)
        self.value.add_edge(dst.id, src.id)
        return True
    def ls(self, path):
        dir = self.mkdir(path)
        res = {}
        for _from, _to, _weight in self.value.edges(from_node=dir.id):
            o = self.value.node(_to)
            if o is None:
                continue
            res[o.name] = o
        return res
    def __purge_nodes(self):
        for n in self.value.nodes(in_degree=0):
            if n == "/":
                continue
            _n = self.value.node(n)
            if _n is not None:
                self.value.del_node(n)

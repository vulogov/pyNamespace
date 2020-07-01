# pyNamespace

pyNamespace is an Application Framework supporting creation of the in-application data storage, simulating organization and behavior of the
Unix filesystem graph. You can create "directories" and data objects. Refer  those directories and data using Unix-like path. Also, you can create internal links between an objects and link one data object to more than one "directory".

## Creation of a namespace

```python
from pyNamespace import *
ns = Namespace()
```
After you import pyNamespace module, you shall create an object of type Namespace. The "filesystem" root - "/" will be created automatically.

## Reading and writing into a namespace

```python
from pyNamespace import *
ns = Namespace()
ns.set("home/answer", 42)
print(ns.get("home/answer"))
```

.set and .get methods will store and read objects from Namespace. Parameters for .set will be the path and a value which will be stored at that path. For .get it'll be a path, from which value will be retrieved.

## Removing objects from namespace

```python
from pyNamespace import *
ns = Namespace()
ns.set("home/answer", 42)
ns.rm("home/answer")
```

.rm with path parameter will remove an object from the namespace. .rm also removes all "orphan" (nodes which do not have an incoming connections) nodes from the graph.

## Refer one node to another in the namespace.

There are two types of the references Soft-reference assumes that the object will be created in the graph, which will have a reference to another object. Method .get will recognize the reference and return the value of the original (source) object. Hard-reference will actually link source object with destination object in the graph.

.link method will create a "soft-link" and .ref will create a hard-reference.

```python
from pyNamespace import *

ns = Namespace()
ns.set("home/answer", 42)
print(ns.link("home/answer", "etc/answer"))
print(ns.get("etc/answer"))
```
This is an example of the soft-reference.

```python
from pyNamespace import *

ns = Namespace()
ns.set("home/answer", 41)
ns.ref("home/answer", "etc")
ns.set("home/answer", 42)
```
This is an example of the hard-reference

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from pyNamespace import *

ns = Namespace()
ns.set("home/answer", 42)
ns.mkdir("home/data")
ns.set("home/data/pi", 3.14)
ns.set("home/data/answer", 42)
ns.set("home/data/hello", "world")
ns.rm("home/data")
print(ns.get("home/answer", 41))

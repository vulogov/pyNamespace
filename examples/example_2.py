import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from pyNamespace import *

ns = Namespace()
ns.set("home/answer", 42)
print(ns.link("home/answer", "etc/answer"))
print(ns.get("etc/answer"))

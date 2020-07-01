import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from pyNamespace import *

def test_obj_1():
    ns = Namespace()
    o = Object(ns, "answer")
    o.value = 42
    assert o.value == 42

def test_obj_2():
    ns = Namespace()
    o = Object(ns, "answer", 42)
    assert o.value == 42

def test_obj_3():
    ns = Namespace()
    o = Object(ns, "answer", 42)
    assert o.isObject() == True

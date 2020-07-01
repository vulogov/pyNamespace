import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from pyNamespace import *

def test_ns_1():
    ns = Namespace()
    dir = ns.mkdir("etc/init.d")
    assert dir.name == "init.d"

def test_ns_2():
    ns = Namespace()
    dir = ns.mkdir("etc/init.d")
    assert dir.fullpath == "etc/init.d"

def test_ns_3():
    ns = Namespace()
    o = ns.set("home/answer", 42)
    assert o.value == 42

def test_ns_4():
    ns = Namespace()
    o = ns.set("home/answer", 42)
    assert o.fullpath == "home/answer"

def test_ns_5():
    ns = Namespace()
    o = ns.set("home/answer", 42)
    assert ns.get("home/answer") == 42

def test_ns_6():
    ns = Namespace()
    assert ns.get("home/answer", 42) == 42

def test_ns_6():
    ns = Namespace()
    ns.set("home/answer", 42)
    ns.mkdir("home/data")
    ns.set("home/data/pi", 3.14)
    ns.set("home/data/answer", 42)
    ns.set("home/data/hello", "world")
    ns.rm("home/data")
    assert ns.get("home/answer", 41) == 42

def test_ns_7():
    ns = Namespace()
    ns.set("home/answer", 42)
    assert ns.link("home/answer", "etc/answer")

def test_ns_8():
    ns = Namespace()
    ns.set("home/answer", 41)
    ns.link("home/answer", "etc/answer")
    ns.set("home/answer", 42)
    assert ns.get("etc/answer") == 42

def test_ns_9():
    ns = Namespace()
    ns.mkdir("home/data")
    ns.set("home/data/pi", 3.14)
    ns.set("home/data/answer", 42)
    ns.set("home/data/hello", "world")
    d = ns.ls("home/data")
    assert len(d) == 3

def test_ns_10():
    ns = Namespace()
    ns.set("home/answer", 41)
    assert ns.ref("home/answer", "etc")

def test_ns_11():
    ns = Namespace()
    ns.set("home/answer", 41)
    ns.ref("home/answer", "etc")
    ns.set("home/answer", 42)
    assert ns.get("etc/answer") == 42

import os
import sys
import ffbklibs
from ffbklibs import helloLib


def test_test():
    s2 = os.path.abspath('.')
    s = 1
    s3 = sys.path
    s3 = helloLib.hello("aa", "bb")
    assert 1 == s

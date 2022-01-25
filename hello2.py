import os
import sys
# from pffbklibs.helloLib import hello
from pffbklibs import helloLib
s2 = os.path.abspath('.')
s = 1
s3 = sys.path
msg = "k"
msg = helloLib.hello("world", "hello2")
print(msg)

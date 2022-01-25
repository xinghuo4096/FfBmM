import sys
import os
from ffbklibs import helloLib

s2 = os.path.abspath('.')
s3 = sys.path

msg = helloLib.hello("world", "hello2")
print(msg)

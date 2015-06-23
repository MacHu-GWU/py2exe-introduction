from __future__ import print_function
import sys

is_py2 = (sys.version_info[0] == 2)
print("hello")
if is_py2:
    raw_input("press any key to exit... ")
else:
    input("press any key to exit... ")
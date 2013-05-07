import imppath
import os

import foo
print(foo.__file__)
os.chdir('..')
print(foo.__file__)

import json
print(json.__file__)

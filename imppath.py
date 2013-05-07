import functools
import importlib
import importlib.abc
import importlib.util
import os
import sys

old_hooks = sys.path_hooks[:]

class AbspathImporter(object):
    def __init__(self, loader):
        self.loader = loader
    def get_filename(self, fullname):
        return os.path.abspath(self.loader.get_filename(fullname))
    def __getattr__(self, attr):
        return getattr(self.loader, attr)

class AbspathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, finder):
        self.finder = finder
    def find_loader(self, fullname):
        loader, portion = self.finder.find_loader(fullname)
        if loader:
            loader = AbspathImporter(loader)
        return loader, portion

old_hook = sys.path_hooks[-1]
def hook(name):
    finder = old_hook(name)
    return AbspathFinder(finder)
sys.path_hooks[-1] = hook

abspathimporter
===============

A Python 3.3 importhook to store absolute paths in `__name__`.

This is really only meant as a proof of concept; the implementation 
is hacky, and makes a lot of assumptions that aren't valid (in
particular, that the last entry in sys.path_hooks is the hook for 
the normal SourceFileFinder, so we can just monkeypatch that and
be done).

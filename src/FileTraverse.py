import os
from RenameFile import RenameFile


def Traverse(files=os.listdir(), curdir="./", a=[], v=False, r=False):
    for root, dirs, files in os.walk(curdir):
        print(root)
        for _f in files:
            extension = _f.split(".")[-1]
            if extension in a:
                path = os.path.join(root, _f)
                RenameFile(path, verbose=v, replace=r)
        print()

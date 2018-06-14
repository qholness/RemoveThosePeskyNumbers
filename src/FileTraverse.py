import os
from RenameFile import RenameFile


def Traverse(files=os.listdir(), curdir="./", a=[], v=False, r=False):
    for f in files:
        cur = os.path.join(curdir, f)
        if os.path.isdir(cur):
            Traverse(files=os.listdir(cur), curdir=cur)
        elif os.path.isfile(cur):
            extension = f.split(".")[-1]
            if extension in a:
                RenameFile(cur, verbose=v, replace=r)

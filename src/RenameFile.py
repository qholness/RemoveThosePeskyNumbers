import re
import os


def RenameFile(path, verbose=False, replace=False):
    fpath = "/".join(path.split('/')[:-1])
    fname = path.split('/')[-1]
    fname, ftype = fname[:-4], fname[-4:]
    newfile = re.sub(r"[0-9]{2} ", "", fname)
    newfile = re.sub(r"[0-9]{2} - ", "", newfile)
    newfile = re.sub(r"[0-1]-[0-9]{2} - ", "", newfile)
    newfile = re.sub(r"[0-1]-[0-9]{2} ", "", newfile)
    newfile = re.sub(r"[0-9]{2}. ", "", newfile)
    newfile = re.sub(r"[0-9]{2}.", "", newfile)
    newfile = re.sub(r"[0-9]{2}-", "", newfile)
    newfile = re.sub(r"[0-9]{1} - ", "", newfile)
    newfile = re.sub(r"[0-9]{1}. ", "", newfile)
    newfile = re.sub(r"CD[0-9]{1} [0-9]{2} - ", "", newfile)
    newfile = re.sub(r"[0-9]{1}-", "", newfile)
    newfile = re.sub(r"- ", "", newfile)
    newpath = os.path.join(fpath, newfile + ftype)

    if verbose is True:
        print(newpath)

    if replace is True:
        os.rename(path, newpath)

    return newfile
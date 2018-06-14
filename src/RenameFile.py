import re
import os


class ReSub(str):
  def __new__(self, *args, **kwargs):
    retNew = str.__new__(self, *args, **kwargs)
    retNew.sub = lambda fro,to: ReSub(re.sub(fro, to, retNew))
    return retNew

def RenameFile(path, verbose=False, replace=False):
    fpath = "/".join(path.split('/')[:-1])
    fname = path.split('/')[-1]
    ftype = fname.split(".")[-1]
    fname = fname.replace(".{}".format(ftype), "")
    newfile = ReSub(fname)
    newfile.sub(r"[0-9]{2} ", "")\
          .sub(r"[0-9]{2} - ", "")\
          .sub(r"[0-1]-[0-9]{2} - ", "")\
          .sub(r"[0-1]-[0-9]{2} ", "")\
          .sub(r"[0-9]{2}. ", "")\
          .sub(r"[0-9]{2}.", "")\
          .sub(r"[0-9]{2}-", "")\
          .sub(r"[0-9]{1} - ", "")\
          .sub(r"[0-9]{1}. ", "")\
          .sub(r"CD[0-9]{1} [0-9]{2} - ", "")\
          .sub(r"[0-9]{1}-", "")\
          .sub(r"[0-9]{2} - - ", "")\
          .sub(r"- ", "")
    newpath = os.path.join(fpath, "{}.{}".format(newfile, ftype))

    if verbose is True:
        print("\t", newfile)

    if replace is True:
        os.rename(path, newpath)

    return newfile
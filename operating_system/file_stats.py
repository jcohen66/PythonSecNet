import os
import time

file="file_stats.py"
st = os.stat(file)
print("file stats: ", file)
mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
print("- Created: %s" % time.ctime(ctime))
print("- Accessed: %s" % time.ctime(atime))
print("- Modified: %s" % time.ctime(mtime))
print("- Size: %s" % size)
print("- Owner: ", gid)
print("- Mode: ", mode)



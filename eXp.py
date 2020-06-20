import sys
sys.path.append("lib")
from lib import zklib
import zkconst

zk = zklib.ZKLib("192.168.1.1", 4370)

ret = zk.connect()
print "connection:", ret
print "Opening Door.....", zk.door()
print "Disconnect:", zk.disconnect()

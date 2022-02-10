#! usr/bin/python
import time
time.sleep(12)
print("Test succeded")
with open("/test2/filestosave/test.txt","w+") as f:
  f.write("test succeded")


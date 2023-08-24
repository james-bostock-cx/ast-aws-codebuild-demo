import os
import sys

for arg in sys.argv[1:]:
  os.unlink(arg)

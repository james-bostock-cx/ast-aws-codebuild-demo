import os
import sys

# A primitive rm(1).
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        os.unlink(arg)

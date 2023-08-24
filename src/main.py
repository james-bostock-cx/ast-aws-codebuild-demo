import os
import sys

# A primitive rm(1).
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: python3 ${sys.argv[0]} <files>', file=sys.stdout)
        sys.exit(1)

    for arg in sys.argv[1:]:
        os.unlink(arg)

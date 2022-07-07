import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

urlbar = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if urlbar.count(".") > 0:
    print("http://" + urlbar)
elif urlbar.count("http://") > 0 or urlbar.count("ftp://") > 0 or urlbar.count("https://") > 0:
    print(urlbar)
else:
    print("ftp://" + urlbar)
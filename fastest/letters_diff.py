import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

upp = re.findall(r'[A-Z]', s)
low = re.findall(r'[a-z]', s)
print(abs(len(upp) - len(low)))
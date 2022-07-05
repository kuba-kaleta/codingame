import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def select1(color):
    if(color == "black"):
        return 0
    if(color == "brown"):
        return 1
    if(color == "red"):
        return 2
    if(color == "orange"):
        return 3
    if(color == "yellow"):
        return 4
    if(color == "green"):
        return 5
    if(color == "blue"):
        return 6
    if(color == "violet"):
        return 7
    if(color == "grey"):
        return 8
    if(color == "white"):
        return 9

def select2(color):
    if(color == "black"):
        return 1
    if(color == "brown"):
        return 10
    if(color == "red"):
        return 100
    if(color == "orange"):
        return 1000
    if(color == "yellow"):
        return 10000
    if(color == "green"):
        return 100000
    if(color == "blue"):
        return 1000000
    if(color == "violet"):
        return 10000000
    if(color == "grey"):
        return 100000000
    if(color == "white"):
        return 1000000000

n = int(input())
for i in range(n):
    str_1, str_2, str_3 = input().split()

    print((10*select1(str_1) + select1(str_2)) * select2(str_3))
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    
    
# TheObserver

import sys
import math

T = [ 'black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white' ]
n = int(input())

for i in range(n):
    c1, c2, c3 = input().split()
    print((T.index(c1)*10 + T.index(c2)) * 10**T.index(c3))

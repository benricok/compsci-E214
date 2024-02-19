import sys
import stdio
import random

def main(): 
    n = int(sys.argv[1])
    a = []
    for i in range(n):
        a.append(random.randfloat(0, 1))
        stdio.writef('%2d\n', a[])
    

if __name__ == '__main__':
    main()

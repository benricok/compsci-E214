import sys
import stdio
import random

def main(): 
    n = int(sys.argv[1])
    a = []
    total = 0.0
    for i in range(n):
        a.append(random.random())
        stdio.writef('%0.4f\n', a[i])
        total += a[i]

    stdio.writef('Average: %0.2f\n', total / n)
    stdio.writef('Min: %0.2f\n', min(a))
    stdio.writef('Max: %0.2f\n', max(a))
    

if __name__ == '__main__':
    main()

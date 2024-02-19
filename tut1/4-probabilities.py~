import stdio, random, sys

N = 10000

total = 0
for i in range(N):
    numrolls = 0
    die = 0
    while die != 2 and die != 4:
        die = 1 + int(random.random() * 6)
        numrolls =+ 1
        total += numrolls
    avg = total / N

stdio.writeln(avg) 

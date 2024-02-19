import sys, stdio, random

log = False
n = len(sys.argv)

a_total = 0
a_prev = False
b_total = 0
b_prev = False

if n >= 2:
    simulations = sys.argv[1]
    stdio.writef('Running %d simulations.', simulations)
    
    if n >= 3:
        log = True

    for i in range(simulations):
        done = False
        stdio.writef('Alice:')
        while !done:
            res = roll()
            if a_total == 0:
                a_prev = res
            a_total += 1
            if log:
                std.write(convert(res))
             

                
        
        done = False
        stdio.writef(' Bob:')   
        while !done:
            res = roll()
            if b_total == 0:
                b_prev = res
            b_total += 1
            if log:
                std.write(convert(res))
            

def roll():
    return round(random.random())

def convert(res):
    if res == 0:
        return 'T'
    elif res == 1:
        return 'H'

    


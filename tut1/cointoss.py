import sys, stdio, random

def roll():
    return round(random.random())

def convert(res):
    if res == 0:
        return 'T'
    elif res == 1:
        return 'H'

log = False
n = len(sys.argv)

a_total = 0
prev = False
b_total = 0

a_win = 0
b_win = 0

if n >= 2:
    simulations = int(sys.argv[1])
    if simulations < 1:
        stdio.writef('Invalid number of simulations.\n')
        sys.exit(1)
    stdio.writef('Running %d simulations.\n', simulations)
    
    if n >= 3:
        log = True

    for i in range(simulations):
        done = False
        if log:
            stdio.writef('Alice: ')
        while not done:
            res = roll()
            if a_total == 0:
                prev = res
            a_total += 1
            if log:
                stdio.writef('%c', convert(res))
            if prev and res:
                done = True
            prev = res
        
        done = False
        if log:
            stdio.writef(' Bob: ')   
        while not done:
            res = roll()
            if b_total == 0:
                prev = res
            b_total += 1
            if log:
                stdio.writef('%c', convert(res))
            if prev != res:
                done = True
            prev = res
        
        if a_total > b_total:
            if log:
                stdio.writef(' Bob has fewer.\n')
            b_win += 1
        elif a_total < b_total:
            if log:
                stdio.writef(' Alice has fewer.\n')
            a_win += 1
        else:
            if log:
                stdio.writef(' Tied.\n')
        done = False
        a_total = 0
        b_total = 0

stdio.writef('Alice won %d times, Bob won %d times.\n', a_win, b_win)
stdio.writef('Probability of Alice winning: %f\n', a_win / simulations)
   


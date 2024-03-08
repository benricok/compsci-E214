import sys, random

if len(sys.argv) > 2:
    T = int(sys.argv[1])
    N = int(sys.argv[2])

    print(f'{T} trials {N} visitors')
    
    p_count = 0
    average = 0

    for trial in range(T):
        s = 1
        heard_story = [0] * N
        heard_story[0] = 1
        last = 0
        from_who = [-1] * N
        from_who[0] = 0

        done = False
        rnd = random.randint(0, N-1)
        while not done:
            while last == rnd or from_who[rnd] == rnd:
                rnd = random.randint(0, N-1)

            if heard_story[rnd]:
                done = True
            else:
                heard_story[rnd] += 1
                from_who[rnd] = last
                s += 1
                last = rnd
        
        average += s
        if all(heard_story):
            p_count += 1

    
    p = p_count / T
    average = average / T
    print(f'average number of story recipients  {average}')
    print(f'Pr(everyone hears story) {p}')


import sys
a = [int(arg) for arg in sys.argv[1:]]
odd_idx = [idx for idx, x in enumerate(a) if x % 2]
for idx, x in zip(reversed(odd_idx), sorted([a[idx] for idx in odd_idx])):
    a[idx] = x
print('_'.join(map(str, a)))









#a = [int(arg) for arg in sys.argv[1:]]
#odd_idx = [idx for idx, x in enumerate(a) if x % 2 != 0]
#odd_val = [a[idx] for idx in odd_idx]
#odd_idx.reverse()
#for idx, x in enumerate(odd_idx):
#    a[x] = odd_val[idx]
#
## PRINT
#for idx, x in enumerate(a):
#    if idx < len(a)-1:
#        print(f'{x}_', end='')
#    else:
#        print(f'{x}')

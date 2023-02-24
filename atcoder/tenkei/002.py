#import 
# import pypyjit
from itertools import product
# pypyjit.set_param('max_unroll_recursion=-1')

#---------------------------------------#
#input

N = int(input())
#--------------------------------------#
#solve

def isValid(S):
    score = 0
    for c in S:
        if c == '(':
            score += 1
        else:
            score -= 1
        
        if score < 0:
            return False
    return (score == 0)


#bit全探索にはproduct
for S in product(['(',')'],repeat=N):
    if (isValid(S)):
        print(*S,sep='')



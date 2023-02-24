#import 
# import pypyjit
import sys
import itertools
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input
N,K = map(int,input().split())
A = list(map(int,input().split()))
#--------------------------------------#
#solve

setA = set(A)

listA = list(setA)
count = 0

for i in range(K):
    
    if i not in setA:
        ans = i
        break
    
else:
    ans = K


print(ans)
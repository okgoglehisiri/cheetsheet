#import 
# import pypyjit
import sys
import itertools
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


#--------------------------------------#
#solve


ans = 0

for i in range(B):
    ans += A[B[i]]
    
print(ans)
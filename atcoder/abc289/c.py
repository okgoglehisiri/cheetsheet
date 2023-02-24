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
C = []
a = []
for i in range(M):
    C.append(int(input()))
    a.append(list(map(int,input().split())))

#--------------------------------------#
#solve

max = 2**M - 1
ans = 0
for i in range(1,M+1):
    
    for pair1 in itertools.combinations(a,i):
        pair = list(pair1)
        tmp = []
        for i in range(len(pair)):
            tmp.extend(pair[i])
        
        s_tmp = set(tmp)
        if len(s_tmp) == N:
            ans += 1
        
        
print(ans)
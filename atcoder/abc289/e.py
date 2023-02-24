#import 
# import pypyjit
import sys
import itertools
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input
T = int(input())


for _ in range(T):
    N,M = map(int,input().split())
    C = list(map(int,input().split()))
    UV = [map(int,input().split()) for _ in range(N)]
    U,V = [list(i) in zip(*UV)]
    
    
#--------------------------------------#
#solve

    if T % 2 == 1:
        print(-1)
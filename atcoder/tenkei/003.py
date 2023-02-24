#import 
# import pypyjit
import sys
from itertools import product
# pypyjit.set_param('max_unroll_recursion=-1')
# 再帰上限変更
sys.setrecursionlimit(1000000)
#---------------------------------------#
#input

N = int(input())
G = [[] for i in range(N-1)]

for i in range(N-1):
    a,b = map(int,input().split())
    a,b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

#--------------------------------------#
#solve

# ある点から最も遠い点とその点から最も遠い点を計算する

def dfs(s):
    dist = [-1] * N
    dist[s] = 0
    st = [s]
    return helper(s,G,dist)


def helper(s,G,dist):
    for nv in G[s]:
        if dist[nv] == -1:
            dist[nv] = dist[s] + 1
            helper(nv,G,dist)
    return dist


dist0 = dfs(0)
index = dist0.index(max(dist0))

r_dist = dfs(index)

print(max(r_dist) + 1)
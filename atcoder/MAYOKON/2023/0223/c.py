import sys
import itertools
import math
from bisect import bisect_left
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
inf = 1 << 60
#pypyjit.set_param('max_unroll_recursion=-1')
#再帰上限変更
sys.setrecursionlimit(1000000)

#==============================================================================#
# UnionFind
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n

    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return 

    def same(self,a,b):
        return self.leader(a) == self.leader(b)

    def size(self,a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]
#==============================================================================#


def main():
    N,K = map(int,input().split())
    
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    DP_A = [False] * N
    DP_B = [False] * N
    DP_A[0] = True
    DP_B[0] = True
    
    for i in range(N-1):
        if DP_A[i]:
            DP_A[i+1] != abs(A[i] - A[i+1]) <= K
            DP_B[i+1] != abs(A[i] - B[i+1]) <= K

        if DP_B[i]:
            DP_B[i+1] != abs(B[i] - B[i+1]) <= K
            DP_A[i+1] != abs(B[i] - A[i+1]) <= K


    if DP_A[N-1] == True or DP_B[N-1] == True:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
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
    A_sort =sorted(A)
    syou = K//N
    amari = K%N

    A_sort_ooi = A_sort[:amari]
    A_sort_ooi_set = set(A_sort_ooi)
    for i in A:
        if i in A_sort_ooi_set:
            print(syou+1)
        else:
            print(syou)
        



if __name__ == '__main__':
    main()
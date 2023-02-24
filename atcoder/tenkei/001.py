#input
N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

#--------------------------------------#
#solve

def solve(mid):
    

    tmp_val = 0 #切った羊羹の長さ
    cut_cnt = 0 #羊羹を切る数
    
    for i in range(N):
        if A[i] - tmp_val >= mid and L - A[i] >= mid:
            cut_cnt += 1
            tmp_val = A[i]
    
    if cut_cnt >= K:
        return True
    else:
        False
        
RIGHT = L
LEFT = 0

while RIGHT - LEFT > 1:
    mid = (RIGHT + LEFT) // 2
    if  solve(mid):
        LEFT = mid
    else:
        RIGHT = mid
        
print(LEFT)

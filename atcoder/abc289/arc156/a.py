








def solve(S,N):
    one = S.count('1')
    zer = S.count('0')
    index = []
    if one % 2 == 1:
        ans = -1
    
    elif one == 2:
        for i in range(N):
            if S[i] == '1':
                index.append(i)
        
        if index[1] - index[0] == 1:
            if zer >= 2:
                ans = 2
            else: ans = -1
        else:
            ans = 1
        
    
    else:
        ans = one / 2
    


    return int(ans)






testcase = int(input())

for _ in range(testcase):
    N = int(input())
    S = input()
    
    print(solve(S,N))
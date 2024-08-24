# DP [N으로 표현]
# https://school.programmers.co.kr/learn/courses/30/lessons/42895

# ⏰ 소요시간 : 57분

    # 1일 때, 
        # N
    # 2일 때,
        # NN
        # N / N , N * N , N + N , N - N
    # 3일 때,
        ## NNN
        ## NN / N , NN * N , NN + N, NN - N
        # (N * N) / N , (N * N) * N , (N * N) + N , (N * N) - N  
        # (N / N) / N , (N / N) * N , (N / N) + N , (N / N) - N  
        # ...
        
    # 4일 때,
        ## NNNN
        ## NNN * N, NNN / N, NNN + N, NNN - N
        ## (NN / N) / N
        
        
def solution(N, number):
    dp = [[], [N]]
    if number == N:
        return 1
    
    for i in range(2, 9):
        dp.append([int(str(N)*i)])
        for j in range(1, i):
            for k in dp[i-j]:
                for t in dp[j]:
                    if t > 0 :
                        dp[i].append(k // t)
                    dp[i].append(k * t)
                    dp[i].append(k - t)
                    dp[i].append(k + t)
                
        if number in dp[i]:
            return i
            
    return -1

solution(5, 12)
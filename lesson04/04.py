def solution(N, A):
    # write your code in Python 3.6
    M = len(A)
    counters = [0] * N
    
    max_result = max_counter = 0
    for i in range(M):
        if A[i] == N + 1:
            max_result = max(max_result, max_counter)
        else:
            if counters[A[i] - 1] < max_result:
                counters[A[i] - 1] = max_result
            
            counters[A[i] - 1] += 1
            max_counter = max(max_counter, counters[A[i] - 1])
            
    for i in range(N):
        counters[i] = max(max_result, counters[i])
        
    return counters
    
"""
# O(N + M) 이기에 for문을 두번 N, M
"""

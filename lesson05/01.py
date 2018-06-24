def solution(A, B, K):
    # write your code in Python 3.6
    result = 0
    start_num = A // K if A % K == 0 else ((A // K) + 1)
    end_num = B // K
    return end_num - start_num + 1

def solution(A, K):
    # write your code in Python 3.6
    res = [0] * len(A)  ## 반환용
    list_len = len(A)  # 1
    for i in range(len(A)):
        if i + K <= list_len - 1:
            idx = i + K
        else:
            idx = (i + K) % list_len  # Mod
        res[idx] = A[i]
    return res

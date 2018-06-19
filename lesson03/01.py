def solution(A):
    # write your code in Python 3.6
    l_len = len(A)
    if l_len == 0:
        return 1

    temp_list = [False] * (l_len + 1)
    for i in range(l_len):
        num = A[i]
        temp_list[num-1] = True

    for i in range(l_len + 1):
        if temp_list[i]^True != 0:
            return i+1
        pass

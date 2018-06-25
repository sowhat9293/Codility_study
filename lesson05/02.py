def solution(A):
    # write your code in Python 3.6
    N = len(A)
    east_list = []
    result_num = 0
    for i in range(N):
        if not A[i]:
            east_list.append(i)
        else:
            result_num += len(east_list)

    return result_num if result_num <= 1000000000 else -1

def solution(A):
    # write your code in Python 3.6
    seen = [False] * len(A)
    for i in range(len(A)):
        if 0 < A[i] <= len(A):
            seen[A[i] - 1] = True

    for i in range(len(seen)):
        if seen[i] is False:
            return 0
    return 1

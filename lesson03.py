def solution(X, Y, D):
    # write your code in Python 3.6
    d = Y - X
    if d % D == 0:
        return int(d / D)

    return int(d / D + 1)

# 이전 방식에는 in 연산자를 통해 비교하였으나 ^2 시간복잡도가 생성
def solution(X, A):
    # write your code in Python 3.6
    if X and len(A) is False:
        return -1
    temp_list = [False] * X
    check_sum = 0   # Check sum을 통한 비교
    for i in range(len(A)):
        if temp_list[A[i] - 1] is False:
            temp_list[A[i] - 1] = True
            check_sum += 1
            if check_sum == X:
                return i
        pass
    return -1

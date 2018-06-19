def solution(A):
    # write your code in Python 3.6
    sum_of_part_one = 0
    sum_of_part_two = sum(A)    # 최초 모든 값을 더함
    min_diff = None             # 차이의 절대값의 최솟값
    for i in range(1, len(A)):  # A[i-1]을 기점으로 한 쪽은 더해주고, 한 쪽은 감한다
        sum_of_part_one += A[i-1]   
        sum_of_part_two -= A[i-1]
        diff = abs(sum_of_part_one - sum_of_part_two)   # 차이의 절대값

        if min_diff is None:    # 최초 비교시
            min_diff = diff
        else:   # 기존 min_diff와 diff 중 작은 값을 구함
            min_diff = min(diff, min_diff)

    return min_diff

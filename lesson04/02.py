# 내가 작성 한 코드
def solution(A):
    # write your code in Python 3.6
    temp_list = [False] * (max(A) + 1)
    for i in range(len(A)):
        if A[i] > 0:
            temp_list[A[i] - 1] = True

    for i in range(len(temp_list)):
        if temp_list[i] is False:
            return i + 1

    return 1
    
   
# 인터넷에서 찾은 코드
def solution(A):
    seen = [False] * len(A)
    for value in A:
        if 0 < value <= len(A):
            seen[value-1] = True
 
    for idx in xrange(len(seen)):
        if seen[idx] == False:
            return idx + 1
 
    return len(A)+1

"""
# 내가 작성한 코드는 O(n) or O(nlogn)이 나왔다. 그 이유는 아마 
# 4 temp_list = [False] * (max(A) + 1) , max(A)일 것으로 추측된다.
"""

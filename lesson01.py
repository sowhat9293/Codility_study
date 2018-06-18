def solution(N):
    # write your code in Python 3.6
    b = "{0:b}".format(N)   # 이진수 변경
    l = []  # Gab을 담을 List 생성
    if b.count("0") != 0: ## 10진수 -> 2진수 변환시 0이 존재 한다면
        for i in range(len(b)): ## Line3에서 만든 이진수 String 탐색
            if b[i] == "1":
                next = b.find("1", i+1) # 1 등장 이후부터 1 Find
                if next != -1:
                    l.extend([next-i-1])
                else: ## 이후 1이 없는 경우
                    l.extend([0])
        return max(l)
    else: ## 0이 없다면 Gab=0 반환
        return 0

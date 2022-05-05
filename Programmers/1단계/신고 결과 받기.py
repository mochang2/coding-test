"""
220503
2022 KAKAO BLIND RECRUITMENT
url: https://programmers.co.kr/learn/courses/30/lessons/92334
후기: 카카오는 1단계도 어렵다... 처음에 시간초과가 났다.
1. 신고 받는 사람의 횟수를 dict에 저장해서 계산
2. dict.keys()를 순회하면서 신고받는 사람이 k 이상 신고받았으면 그를 신고한 사람들을 추적
2번의 과정에서 dict를 다시 순회하니까 시간초과가 난 것 같다. dict에서 search는 충돌이 날 경우 O(N)까지도 되기 때문이다.

결국 신고받은 횟수를 계산할 때 그를 신고한 사람들도 변수에 같이 저장(공간 복잡도를 포기)하니까 해결됐다.
"""

def solution(id_list, reports, k):
    answer = [0 for _ in range(len(id_list))]
    reports = set(reports)
    map_ = dict() # 아이디와 인덱스를 매핑
    accused = dict() # 신고한 사람
    accused_num = dict() # 신고 당한 횟수
    
    for index, id in enumerate(id_list):
        map_[id] = index
        accused[id] = list()
        accused_num[id] = 0
        
    for report in reports:
        normal_user, abnormal_user = report.split(" ")
        accused[abnormal_user].append(normal_user)
        accused_num[abnormal_user] += 1
    
    for key, value in accused_num.items():
        if value >= k:
            for normal_user in accused[key]:
                answer[map_[normal_user]] += 1
    
    return answer
  

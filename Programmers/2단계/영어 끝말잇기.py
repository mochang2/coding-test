"""
211126
Summer / Winter Coding(~2018)
url: https://programmers.co.kr/learn/courses/30/lessons/12981
후기: 다른 풀이를 보면 list에서 확인했는데 입력이 길어지면 시간 초과가 날 것 같다고 생각함. 근데 어차피 dict도 시간 복잡도는 똑같으니 의미가 없었음.
"""

def solution(n, words):
    rotation = 1
    number = 1 # index
    dic = {words[0]: 1}
    for index, word in enumerate(words[1:]):
        if word in dic.keys() or word[0] != words[index][-1]: # 게임이 끝남
            return [number + 1, rotation]
        
        dic[word] = 1
        number = (number + 1) % n
        if number == 0:
            rotation += 1
            
    return [0,0]  # 패배자가 없음
  

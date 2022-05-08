"""
220508
2019 KAKAO BLIND RECRUITMENT
url: https://programmers.co.kr/learn/courses/30/lessons/42889
후기: 왜 이렇게 더럽게밖에 안 풀리지 싶었는데, 다른 사람의 풀이를 보고 js의 아름다움을 느꼈다.
내장 함수를 얼마나 잘 쓰냐의 차이인 것 같다.
시간 복잡도는 똑같다.
"""

// 내 풀이
function sortFunc(a, b) {
    if (a[1] < b[1]) return 1
    else if (a[1] > b[1]) return -1
    else {
        if (a[0] > b[0]) return 1
        else return -1
    }
}

function solution(N, stages) {
    const answer = Array.from({length: N + 1}, (v, i) => [0,0])

    let count = 0 // 모든 스테이지를 클리어한 사람의 수
    for (const stage of stages) {
        if (stage > N) {
            count++
            continue
        }
        
        for (let i = 1; i <= stage; i++) {
            answer[i][1] += 1
        }
        answer[stage][0] += 1
    }
    for (const index in answer.slice(1,)) {
        const current = answer[parseInt(index) + 1]
        if (current[1] + count === 0) { // 분모가 0일 경우 예외처리
            answer[index] = 0
            continue
        }
        answer[index] = current[0] / (current[1] + count)
    }
    answer.pop()
    for (let i = 0; i < N; i++) {
        answer[i] = [i + 1, answer[i]] // 처음에 index를 같이 안 넣어줘서 뒤에서 다시 넣어줬다.
    }
    answer.sort(sortFunc)
    
    return answer.map(value => value[0])
}


// 다른 사람 풀이
function solution(N, stages) {
  let stageNFailRate = []; // const로 선언해도 문제 없음
  for (let stage = 1; stage <= N; stage++) {
    const playerReached = stages.filter((player) => player >= stage).length;
    const playerChallenging = stages.filter(
      (player) => player === stage
    ).length;
    stageNFailRate.push([stage, playerChallenging / playerReached]);
  }
  stageNFailRate.sort((a, b) => b[1] - a[1]);
  return stageNFailRate.map((stage) => stage[0]);
}


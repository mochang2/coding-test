/*
220507
양궁대회
url: https://programmers.co.kr/learn/courses/30/lessons/92342
후기: 우테캠이 js로만 볼 수 있어서 갑자기 js 코테 공부를 시작했다.

어려웠다. 백트래킹의 정석이라는 N-Queen도 풀어봤지만, 역시 그 때 답을 봤던 게 실력향상에 큰 도움이 안 됐던 것 같다.
더 많은 문제를 접해봐야겠다.
백트래킹의 요점은 dfs를 언제 종료할지, 어떤 기준(변수)로 종료 시점을 정할지, 어떤 상황에 dfs를 들어갈지, 
몇 개의 depth를 들어갈지, 어떤 것을 인자로 전달하고 / 어떤 것을 전역변수로 설정할지 등인 것 같다.

처음에 쏜 화살의 개수가 주어진 arrowN개라면 백트래킹을 종료하려고 했으나 백트래킹 진입 조건을 잘못 생각해서 삽질을 많이 했다.
이 풀이의 요점은 65~75번째 줄이다.
*/

let lion = []
let answer = []
let maxScoreDiff = 0

function calcScoreDiff(appeach) {
    let appeachScore = 0
    let lionScore = 0
    for (let i = 0; i < 10; i++) { // i == 11을 가정할 필요 없음
        if (lion[i] > appeach[i]) {
            lionScore += (10 - i)
        } else {
            if (appeach[i] !== 0) {
                appeachScore += (10 - i)
            }
        }
    }
    
    return lionScore - appeachScore
}

function dfs(appeach, arrowN, pointIndex) {
    if (pointIndex === 11) { // 10~1점까지 다 쐈으면 점수 계산해서 answer 업데이트
        if (arrowN !== 0) {
            lion[10] = arrowN // 주어진 개수만큼 다 못 쏠 경우. 무조건 0점을 쐈다고 가정
        }
        
        const scoreDiff = calcScoreDiff(appeach)
        if (scoreDiff < maxScoreDiff) {
            return
        }
        else if (scoreDiff > maxScoreDiff) {
            maxScoreDiff = scoreDiff
            answer = JSON.parse(JSON.stringify(lion)) // deepcopy
            return
        }
        else {
            // 낮은 점수가 더 많은 게 answer인지 lion인지 찾음
            for (let i = 10; i >= 0; i--) {
                if (lion[i] === answer[i]) continue
                
                if (lion[i] > answer[i]) {
                    answer = JSON.parse(JSON.stringify(lion))
                }
                break
            }
            return
        }
    }
    
    if (arrowN > appeach[pointIndex]) {
        // 점수 얻는 경우. 어피치보다 한 발 더 쏨
        lion[pointIndex] = appeach[pointIndex] + 1
        dfs(appeach, arrowN - appeach[pointIndex] - 1, pointIndex + 1)
        lion[pointIndex] = 0
    }
    
    // else 사용하면 안됨. 점수 못 얻는 경우. 해당 점수에는 아예 쏘기를 포기
    lion[pointIndex] = 0
    dfs(appeach, arrowN, pointIndex + 1)
    lion[pointIndex] = 0
}

function solution(arrowN, info) {
    lion = Array.from({length: 11}, () => 0)
    dfs(info, arrowN, 0) // 10점부터 쏴서 모든 경우의 수를 찾음
    
    return answer.length === 0 ? [-1] : answer
}

/*
221125
url: https://school.programmers.co.kr/learn/courses/30/lessons/12927
후기: 그리디 문제였다.
투포인터와 같은 그리디 문제에서 내가 가장 많이 틀리고 실수하는 부분이 조건 찾기이다.
그래서 이 문제도 많이 틀렸다.

적정한 maxPointer를 위치시키기 위해 많은 조건문을 썼지만 빈번히 예외가 발생했다.
그래서 답을 봤고 간단히 이중 반복문으로 해결할 수 있었다.
*/

function sortDecreasingOrder(number1, number2) {
    return number2 - number1
}

function minimizeOverworkIndex(residue, works) {
    const minimizedWorks = works.sort(sortDecreasingOrder)
    
    while (residue > 0) {
        // maxPointer === minimizedWorks.length와 같을 때, 아닐 때
        // minimizedWorks[maxPointer]와 [maxPointer + 1], [maxPointer - 1] 크기 비교
        // 이러한 모든 예외를 처리하다가 결국 계속 틀렸음
      
        for (let maxPointer = 0; maxPointer < minimizedWorks.length; maxPointer++) {
            minimizedWorks[maxPointer]--
            residue--
            
            if (minimizedWorks[maxPointer] >= minimizedWorks[maxPointer + 1] ||
                residue <= 0) {
                break
            }
        }
    }

    return minimizedWorks
}

function calculateOverworkIndex(works) {
    return works.reduce((accumulation, work) => accumulation + Math.max(0, work) ** 2, 0) // 음수 처리
}

function solution(n, works) {
    const minimizedWorks = minimizeOverworkIndex(n, works)
    // .map(work => Math.max(0, work))를 한다면 calculateOverworkIndex에서 음수 처리를 안 해도 됐음
    // 이게 더 클린 코드 스러운 듯
    
    return calculateOverworkIndex(minimizedWorks)
}

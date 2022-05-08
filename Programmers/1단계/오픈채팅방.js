/*
220508
2019 KAKAO BLIND RECRUITMENT
url: https://programmers.co.kr/learn/courses/30/lessons/42888
후기: js에 익숙한 사람이 보기에 편안한 코드일 것 같지는 않다.
filter(continue가 있는 줄)를 쓴 뒤에 map을 쓸까했는데 그러면 O(n^2)의 시간 복잡도이기 때문에 O(n)으로 끝내기 위해 아래와 같이 사용했다.
*/

// 내 풀이
function solution(records) {
    const answer = []
    const dict = {}
    
    for (const record of records) {
        const operation = record.split(" ")
        if (operation[0] === 'Leave') continue
        dict[operation[1]] = operation[2]
    }
    for (const record of records) {
        const operation = record.split(" ")
        if (operation[0] === 'Change') continue        
        const action = operation[0] === 'Enter' ? '들어왔습니다.' : '나갔습니다.'
        answer.push(`${dict[operation[1]]}님이 ${action}`)
    }
    
    return answer
}


// +) 추가 다른 사람 풀이. map을 이용해서 좀더 js 스럽게 표현했다.
function solution(record) {
    var answer = [];
    const users = {}
    record.map(history => {
        const [action, id, name] = history.split(' ')
        if(action !== 'Leave') users[id] = name
    })
    record.map(history => {
        const [action, id, name] = history.split(' ')
        if(action === 'Enter') answer.push(`${users[id]}님이 들어왔습니다.`)
        if(action === 'Leave') answer.push(`${users[id]}님이 나갔습니다.`)
    })
    return answer;
}


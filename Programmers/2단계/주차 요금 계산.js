/*
220505
정렬
url: https://programmers.co.kr/learn/courses/30/lessons/92341
후기: 우테캠이 js로만 볼 수 있어서 갑자기 js 코테 공부를 시작했다.

자주 나오는 parseInt(string), number.toString(), {}, Object.keys, Object.values, Object.entries
push, pop, unshift, shift, slice, map, splice 
Math.ceil, Math.floor, array.sort(sort Function) 등 다시 상기하는 기회였다.
*/

function makeObjKey(info, carNum) {
    info[carNum] = {in: 0, time: 0, cost: 0}
    return info
}

function hourToMinute(hour) {
    hour = hour.split(":")
    return parseInt(hour[0] * 60) + parseInt(hour[1])
}

function sortFunc(a, b) {
    if (a[0] > b[0]) return 1
    else if (a[0] < b[0]) return -1
    else return 0
}

function solution(fees, records) {
    let info = {};
    // '차량번호': {'in': 입차 횟수 - 출차 횟수, 'time': 출차 시간 - 입차 시간, 'cost': 요금}
    const lastTime = hourToMinute('23:59')
    
    for (let record of records) {
        record = record.split(" ");
        let time = record[0];
        const carNum = record[1];
        const type = record[2];
        time = hourToMinute(time);
        
        if (!Object.keys(info).includes(carNum)) {
            info = makeObjKey(info, carNum);
        }
        
        if (type === 'IN') {
            info[carNum]['in']++;
            info[carNum]['time'] -= time;
        } else {
            info[carNum]['in']--;
            info[carNum]['time'] += time;
        }
    }
    for (const carNum of Object.keys(info)) {
        if (info[carNum]['in'] > 0) { // 23:59까지 출차를 안 했다면
            info[carNum]['time'] += lastTime
        }
        
        if (info[carNum]['time'] <= fees[0]) { // 가격 책정
            info[carNum]['cost'] = fees[1]
        } else {
            info[carNum]['cost'] = fees[1] + Math.ceil((info[carNum]['time'] - fees[0]) / fees[2]) * fees[3]
        }
    }
    
    answer = []
    for (const [key, value] of Object.entries(info)) {
        answer.push([key, value['cost']])
    }
    answer.sort(sortFunc)
    
    return answer.map(value => value[1])
}


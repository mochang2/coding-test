/*
221125
url: https://school.programmers.co.kr/learn/courses/30/lessons/42839
후기: 완전 탐색 문제였다.
순열을 직접 구현해보니 왜 이렇게 어려운지 모르겠다.
에라토스테네스와 순열을 이용해 구현했다.

문제는 다음과 같이 해결했다.
1. 에라토스테네스로 10,000,000보다 작은 소수들을 구한다.
2. numbers를 이용한 모든 숫자 조합(순열)을 구한다. 단, 겹치지 않도록 unique한 애들만 구한다.
3. 해당 순열의 구성이 소수인지 판단한다.

2를 재귀 함수로 구현하기 위해 내부 함수를 선언했던 점이 좀 불편했고, 다른 방법이 있을 것 같은데 클린하지 못한 것 같아 아쉬웠다.
*/

const MAX = Number('10,000,000'.replace(/\,/g, ''))

function getUniquePermutations(numbers) {    
    function permutate(length, depth, numbers) {
        if (length === 0) {
            const number = Number(numbers.slice(0, depth).join(''))
            permutations.push(number)

            return
        }

        for (let index = depth; index < numbers.length; index++) {
            ;[numbers[index], numbers[depth]] = [numbers[depth], numbers[index]] // ;를 추가하지 않으면 에러남
            permutate(length - 1, depth + 1, numbers)
            ;[numbers[index], numbers[depth]] = [numbers[depth], numbers[index]] // ;를 추가하지 않으면 에러남
        }
    }
    
    const permutations = []
    const uniquePermutations = new Set()
    
    for (let length = 1; length <= numbers.length; length++) {
        permutate(length, 0, numbers)
    }
    
    for (const permutation of permutations) {
        if (!uniquePermutations.has(permutation)) {
            uniquePermutations.add(permutation)
        }
    }
    
    return [...uniquePermutations]
}

function initializeIsPrime(length) {
    if (length <= 2) {
        return Array.from({ length }).fill(false)
    }
    
    const isPrime = Array.from({ length }).fill(true)
    isPrime[0] = false
    isPrime[1] = false
    
    return isPrime
}

function checkIfPrime() {
    const isPrime = initializeIsPrime(MAX)
    
    for (let prime = 2; prime < isPrime.length; prime++) {
        if (!isPrime[prime]) {
            continue
        }
        
        for (let number = prime * 2; number < isPrime.length; number += prime) {
            isPrime[number] = false
        }
    }
    
    return isPrime
}

function solution(numbers) {
    let answer = 0
    const permutations = getUniquePermutations(numbers.split('')) // 입력된 수들로 만들 수 있는 모든 
    const isPrime = checkIfPrime()
    
    for (const permutation of permutations) {
        if (isPrime[permutation]) {
            answer++
        }
    }
    
    return answer
}

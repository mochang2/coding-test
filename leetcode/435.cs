/*
medium Non-overlapping Intervals
url: https://leetcode.com/problems/non-overlapping-intervals/
후기: 일전에 겹치는 강의 시간 개수를 구하는 문제를 풀어서 (시작 시간, 끝나는 시간) 기준으로 정렬한 적이 있었다.
그래서 틀렸고 정해진 시간이 지나서 그냥 답을 봤다.
이번에도 그럴 거라고 생각했지만, 끝나는 시간만 고민하면 되는 문제였다. 젤 일찍 시작해서 젤 늦게 끝나는 일이 생길 수도 있기 때문이다.
*/

public class Solution {
    public int EraseOverlapIntervals(int[][] intervals) {
        int answer = 0;
        intervals = intervals.OrderBy(i => i[1]).ToArray();  // 끝나는 시간 기준으로만 잡으면 
        int end = -500000;
        
        for (int i = 0; i < intervals.Length; i++) {
            if (end <= intervals[i][0]) end = intervals[i][1];
            else answer++;
        }
        
        return answer;
    }
}

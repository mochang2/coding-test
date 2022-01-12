/*
medium Merge Intervals
url: https://leetcode.com/problems/merge-intervals/
후기: append, remove가 쉬운 List는 일반적으로 array보다 performance가 구리다고 한다.
어차피 제자리 List에서 넣고 빼고 하면 O(N^2)이 걸릴 것 같아, O(N) 안에 되는 코드를 곰곰히 생각해봤다.
stack을 쓰니까 그런 방법이 가능한 것 같아 구현했는데, 생각보다는 효율적이지 않았던 것 같다.
두 번째 풀이는 따봉을 제일 많이 받은 C# 코드다. 나랑 속도는 크게 차이는 안 나지만 조금 더 효율적이었다.
Linq를 이용한 2차원 배열 sort를 배울 수 있었다.
*/

// 내 풀이
public class Solution {
    public int[][] Merge(int[][] intervals) {
        intervals = intervals.OrderBy(i => i[0]).ThenBy(i => i[1]).ToArray();  # 2차원 배열 정렬, 23번째 줄에서 어차피 max를 쓰니까 두 번째 인자까진 비교할 필요 없을 것 같다
        Stack<int[]> s = new Stack<int[]>();
        s.Push(intervals[0]);
        
        for(int i = 1; i < intervals.Length; i++) {
            int[] top = s.Peek();
            if (top[1] >= intervals[i][0]) {
                // stack replace가 없어서 삭제하고 집어넣었다. 아마 s.Peek 자체에서 바꾸는 법이 있을 것도 같은데 귀찮아서 찾아보진 않았다.
                s.Pop();
                s.Push(new int[] { top[0], Math.Max(intervals[i][1], top[1])});
            }
            else s.Push(intervals[i]);
        }
        
        return s.ToArray();  // stack to array
    }
}

// 다른 사람 풀이(약간 더 빠름)
public class Solution {
    public int[][] Merge(int[][] intervals) {
        if (intervals == null || intervals.Length == 0 || intervals.Length == 1)
            return intervals;
        
        List<int[]> res = new List<int[]>();
        
        intervals = intervals.OrderBy(x => x[0]).ToArray();
        
        int s = intervals[0][0],
            e = intervals[0][1];
        
        for (int i = 1; i < intervals.Length; i++)
            if (intervals[i][0] > e)
            {
                res.Add(new int[] { s, e });
                s = intervals[i][0];
                e = intervals[i][1];
            }
            else
                e = Math.Max(e, intervals[i][1]);
        
        res.Add(new int[] { s, e });
        
        return res.ToArray();
    }
}

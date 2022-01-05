/*
easy First Unique Character in a String
url: https://leetcode.com/problems/first-unique-character-in-a-string/
후기: 파이썬 문자열 다루는 것의 장점을 다시금 느낀 문제였다.
string과 char[], char를 구분을 했어야 했다. dictionary는 이미 써본 적 있어서 쉬웠다.
*/

public class Solution {
    public int FirstUniqChar(string s) {
        int answer = 100001;
        Dictionary<char, List<int>> dic = new Dictionary<char, List<int>>();
        char[] char_arr = s.ToCharArray(0, s.Length);
        
        for (int i = 0; i < char_arr.Length; i++) {
            char c = char_arr[i];
            if (!dic.ContainsKey(c)) dic.Add(c, new List<int>() {i});
            else dic[c].Add(i);
        }
        
        foreach(KeyValuePair<char, List<int>> kv in dic) {
            if (kv.Value.Count != 1) continue;
            else {
                if (kv.Value[0] < answer) answer = kv.Value[0];
            }
        }
        return answer == 100001 ? -1 : answer;
    }
}
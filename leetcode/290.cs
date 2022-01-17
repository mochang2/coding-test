/*
easy Word Pattern
url: https://leetcode.com/problems/word-pattern/
후기: 처음에는 dictionary를 하나만 만들었다가 틀렸다. 
다음에는 hashset을 만들었다가 dictionary 2개가 필요하다는 것을 다시 깨닫고 문제를 해결했다.
pattern -> s / s -> pattern 1대1 함수를 만족해야했기 때문이다.
빠르지 않은 것 같아 다른 사람들의 풀이도 봤지만 다들 비슷한 풀이였다.
*/

public class Solution {
    public bool WordPattern(string pattern, string s) {
        int n = pattern.Length;
        Dictionary<char, string> dic_pattern = new Dictionary<char, string>();
        Dictionary<string, char> dic_s = new Dictionary<string, char>();
        string[] s_li = s.Split(' ');
        if (n != s_li.Length) return false;
        
        for (int i = 0; i < n; i++) {
            if (!dic_pattern.ContainsKey(pattern[i])) dic_pattern.Add(pattern[i], s_li[i]);
            else {
                if (dic_pattern[pattern[i]] != s_li[i]) return false;
            }
            
            if (!dic_s.ContainsKey(s_li[i])) dic_s.Add(s_li[i], pattern[i]);
            else {
                if (dic_s[s_li[i]] != pattern[i]) return false;
            }
        }
        
        return true;
    }
}

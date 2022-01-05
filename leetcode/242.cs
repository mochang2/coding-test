/*
easy Valid Anagram
url: https://leetcode.com/problems/valid-anagram/
후기: 350이랑 거의 똑같이 풀었다. sort를 쓰면 더 간결했겠지만 O(n)으로 풀기 위해 dictionary를 사용했다.
*/

public class Solution {
    public bool IsAnagram(string s, string t) {
        // dictionary: O(N)
        // sort: N * log(N)
        char[] s_char_arr = s.ToArray();
        char[] t_char_arr = t.ToArray();
        Dictionary<char, int> s_dic = new Dictionary<char, int>();
        Dictionary<char, int> t_dic = new Dictionary<char, int>();
        
        foreach(char c in s_char_arr) {
            if (!s_dic.ContainsKey(c)) s_dic.Add(c, 1);
            else s_dic[c]++;
        }
        foreach(char c in t_char_arr) {
            if (!t_dic.ContainsKey(c)) t_dic.Add(c, 1);
            else t_dic[c]++;
        }
        
        foreach(KeyValuePair<char, int> kvp in s_dic) {
            if (!t_dic.ContainsKey(kvp.Key)) return false;
            else {
                if (kvp.Value != t_dic[kvp.Key]) return false;
            }
        }
        foreach(KeyValuePair<char, int> kvp in t_dic) {
            if (!s_dic.ContainsKey(kvp.Key)) return false;
            else {
                if (kvp.Value != s_dic[kvp.Key]) return false;
            }
        }
        
        return true;
    }
}
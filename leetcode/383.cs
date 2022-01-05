/*
easy Ransom Note
url: https://leetcode.com/problems/ransom-note/
후기: 387이랑 거의 비슷한 문제였다.
*/

public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        char[] rn_char_arr = ransomNote.ToCharArray(0, ransomNote.Length);
        char[] mz_char_arr = magazine.ToCharArray(0, magazine.Length);
        Dictionary<char, int> rn_dic = new Dictionary<char, int>();
        Dictionary<char, int> mz_dic = new Dictionary<char, int>();
        
        foreach(char c in rn_char_arr) {
            if (!rn_dic.ContainsKey(c)) rn_dic.Add(c, 1);
            else rn_dic[c]++;
        }
        foreach(char c in mz_char_arr) {
            if (!mz_dic.ContainsKey(c)) mz_dic.Add(c, 1);
            else mz_dic[c]++;
        }
        
        foreach(KeyValuePair<char, int> kvp in rn_dic) {
            if (!mz_dic.ContainsKey(kvp.Key)) return false;
            else {
                if (kvp.Value <= mz_dic[kvp.Key]) continue;
                else return false;
            }
        }
        
        return true;
    }
}
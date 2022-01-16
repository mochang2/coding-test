/*
easy Longest Palindrome
url: https://leetcode.com/problems/longest-palindrome/
후기: 해당 char이 홀수개인지, 짝수개인지만 구분하면 됐다. 나는 dictionary를 사용했다.
68%보다만 빨라서 더 빠른 방법이 있나 찾아봤는데 set을 쓰면 훨씬 빨랐을 것 같다.
*/

내 풀이
public class Solution {
    public int LongestPalindrome(string s) {
        Dictionary<char, int> dic = new Dictionary<char, int>();
        foreach(char c in s) {
            if (!dic.ContainsKey(c)) dic.Add(c, 1);
            else dic[c]++;
        }
        
        int answer = 0;
        bool odd_flag = false;
        foreach(KeyValuePair<char, int> kvp in dic) {
            if (kvp.Value % 2 == 0) answer+=kvp.Value;
            else {
                answer += kvp.Value - 1;
                odd_flag = true;
            }
        }
        if (odd_flag) answer++;
        
        return answer;
    }
}


// 다른 사람의 java 풀이
// HashMap이 아니라 HashSet을 썼으니 이게 훨씬 빠를 거 같다.
public int longestPalindrome(String s) {
        if(s==null || s.length()==0) return 0;
        HashSet<Character> hs = new HashSet<Character>();
        int count = 0;
        for(int i=0; i<s.length(); i++){
            if(hs.contains(s.charAt(i))){
                hs.remove(s.charAt(i));
                count++;
            }else{
                hs.add(s.charAt(i));
            }
        }
        if(!hs.isEmpty()) return count*2+1;
        return count*2;
}

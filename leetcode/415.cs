/*
easy Add Strings
url: https://leetcode.com/problems/add-strings/
후기: 파이썬이 정말 그립다... 귀찮아서 64 bit int형으로 변환해서 덧셈해도 overflow가 났다. 결국 코드를 짜야됐다.
다른 빠른 답들과 논리는 같지만, 자릿수를 맞추기 위해 0을 추가하는 코드를 바꾸면 훨씬 빨랐을 것 같다.
*/

public class Solution {
    public void swap(ref string s1, ref string s2) {
        string temp = s1;
        s1 = s2;
        s2 = temp;
    }
    
    public string AddStrings(string s1, string s2) {
        if (s1.Length < s2.Length) swap(ref s1, ref s2);
        int n1 = s1.Length;
        int n2 = s2.Length;
        while (n1 != n2) {
            s2 = "0" + s2;
            n2++;
        }
        
        int carry = 0;
        string answer = "";
        for (int i = n1 - 1; i >= 0; i--) {
            int temp = carry + int.Parse(s1[i].ToString()) + int.Parse(s2[i].ToString());
            if (temp >= 10) {
                carry = 1;
                temp %= 10;
            }
            else carry = 0;
            
            answer = temp + answer;
        }
        if (carry == 1) answer = "1" + answer;
        
        return answer;
    }
}

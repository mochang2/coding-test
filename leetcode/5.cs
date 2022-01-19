/*
medium Longest Palindromic Substring
url: https://leetcode.com/problems/longest-palindromic-substring/
후기: 찝찝함이 남는 풀이였다. 다 풀고 나니 아래에 주석으로 남긴 생각이 들었다.
*/

public class Solution {
    public string LongestPalindrome(string str) {
        int len = str.Length;
        string answer = str.Substring(0, 1);
        
        for (int i = 0; i < len - 1; i++) {
            for (int j = i + 1; j < len; j++) {
                string substr = str.Substring(i, j - i + 1);
                int subLen = substr.Length;
                bool flag = true;
                for (int k = 0; k < subLen / 2; k++) {
                    if (substr[k] != substr[subLen - 1 - k]) {
                        flag = false;
                        break;
                    }
                }
                if (flag) answer = subLen > answer.Length ? substr : answer;
            }
        }
        
        return answer;
    }
}
// 당연히 시간초과가 날 거라고 생각하고 제출했는데 나지 않음
// 제출이 끝난 후에 생각해보니
// 1. string을 순회하면서 시작점을 잡음.
// 2. 해당 시작점을 기준으로 (짝수, 홀수) 길이의 palindromic을 계산
// 3. palindromic이 맞으면 기존에 있던 애와 길이 비교
// 4. return
// 하면 될 듯

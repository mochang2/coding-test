/*
easy Valid Parentheses
url: https://leetcode.com/problems/valid-parentheses/
후기: C# stack은 c++ stack하고 비슷했다. 그리고.. 파이썬의 list가 그리워졌다.
C# 또한 string을 index로 접근이 가능하지만 각각의 타입은 char이다.
TryPop, TryPeek은 구글링으로 잘 안 나온다. 외우는 게 편할 것 같다.
*/


public class Solution {
    public bool IsValid(string s) {
        Stack<char> sc = new Stack<char>();
        
        char tmp;
        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            if (c == '(' || c == '[' || c == '{') sc.Push(c);
            else {
                if (sc.TryPop(out tmp)) {
                    if (c == ')') {
                        if (tmp != '(') {
                            return false;
                        }
                    }
                    else if (c == ']') {
                        if (tmp != '[') {
                            return false;
                        }
                    }
                    else { // c == '}'
                        if (tmp != '{') {
                            return false;
                        }
                    }   
                }
                else return false;
            }
        }
        
        return !sc.TryPeek(out tmp);
    }
}

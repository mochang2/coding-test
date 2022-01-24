/*
medium Minimum Remove to Make Valid Parentheses
url: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
후기: 생각보다 느렸다. C#이나 JAVA는 string을 동적할당하므로 변경이 생기면 성능이 크게 저하된다고 한다.
그래서 보통 StringBuilder를 많이 쓴다고 한다. 다음번에 문자열을 다룰 일이 있으면 사용해봐야겠다.
*/

using System.Text.RegularExpressions;

public class Pair {
    public char c;
    public int i;
    public Pair(char c, int i) {
        this.c = c;
        this.i = i;
    }
}

public class Solution {
    public string MinRemoveToMakeValid(string s) {
        char[] char_array = s.ToCharArray();
        Stack<Pair> stack = new Stack<Pair>();
        for(int i = 0; i < s.Length; i++) {
            char c = s[i];
            if (c == '(') {
                stack.Push(new Pair(c, i));
            }
            else if (c == ')') {
                if(stack.Count != 0 && stack.Peek().c == '(') stack.Pop();
                else stack.Push(new Pair(c, i));
            }
            else continue;
        }
        while (stack.Count != 0) {
            Pair p = stack.Pop();
            char_array[p.i] = 'X';
        }
        s = new string(char_array);
        string answer = Regex.Replace(s, @"X", "");
        
        return answer;
    }
}




// StringBuilder를 쓴 다른 사람 풀이. 훨씬 빠르다.
public class Solution {
    public string MinRemoveToMakeValid(string s) {
            StringBuilder builder = new StringBuilder(s);
            Stack<Tuple<char, int>> stack = new Stack<Tuple<char, int>>();

            for (int i = 0; i < s.Length; i++)
                if (stack.Count > 0 && stack.Peek().Item1 == '(' && s[i] == ')')
                    stack.Pop();
                else if (s[i] == '(' || s[i] == ')')
                    stack.Push(new Tuple<char, int>(s[i], i));

            while (stack.Count > 0)
                builder.Remove(stack.Pop().Item2, 1);

            return builder.ToString();
    }
}

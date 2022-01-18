/*
medium Multiply Strings
url: https://leetcode.com/problems/multiply-strings/
후기: 파이썬의 감사함을 또다시 느꼈다. 그냥 빡구현이었고, 시간을 많이 잡아먹었지만을 
요새 너무 답을 많이 본 거 같아, 오기가 생겨서 그냥 풀었다. 별로인 문제였다.
*/

public class Solution {
    public string Multiply(string num1, string num2) {        
        if (num1 == "0" || num2 == "0") return "0";
        
        List<string> li = new List<string>();
        int max_len = 0;
        //  n u m 2  // j
        // *n u m 1  // i
        for (int i = num1.Length - 1; i >= 0; i--) {
            int carry = 0;
            int n1 = (int)Char.GetNumericValue(num1[i]);
            string result = "";
            int zero_count = num1.Length - 1;
            
            while (zero_count != i) {
                // result에 0을 붙이고 시작
                result += "0";
                zero_count--;
            }
            
            // 한자리씩 곱셈
            for (int j = num2.Length - 1; j >= 0; j--) {
                int temp = (int)Char.GetNumericValue(num2[j]) * n1 + carry;
                carry = temp / 10;
                temp %= 10;
                
                result = temp + result;
            }
            if (carry != 0) result = carry + result;
            
            li.Add(result);
            max_len = Math.Max(max_len, result.Length);
        }
        
        string answer = new string('0', max_len);
        // 덧셈 코드
        for(int i = 0; i < li.Count; i++) {
            string str = li[i];
            int n = answer.Length;
            
            while(str.Length != n) str = "0" + str; // 자릿수를 맞춰주기 위함
            int carry = 0;
            string sum_ = "";
            for (int j = n - 1; j >= 0; j--) {
                int temp = (int)Char.GetNumericValue(answer[j]) + (int)Char.GetNumericValue(str[j]) + carry;
                if (temp >= 10) {
                    carry = 1;
                    temp %= 10;
                }
                else carry = 0;
                sum_ = temp + sum_;
            }
            if (carry != 0) sum_ = carry + sum_;
            answer = sum_;
        }
        
        return answer;
    }
}

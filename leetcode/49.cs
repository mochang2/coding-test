/*
medium Group Anagrams
url: https://leetcode.com/problems/group-anagrams/
후기: 알고리즘은 맞았는데 구현을 못 했다. C# 리트코드는 왜 interface를 return하라고 하는지 전혀 이해가 안된다...
answer에 완성된 1차원 list를 넣는거는 되는데 answer에서 직접 인자를 변형하는 것은 에러를 도출해서 짜증나서 답을 봤다.
알고리즘은 모든 인풋을 순회해서 알파벳 순으로 sort하고 dictionary key 값을 사용해서 애너그램이 되는지 안되는지 확인하면 된다.
*/


public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        List<IList<string>> answer = new List<IList<string>>();
        Dictionary<string, List<string>> dic = new Dictionary<string, List<string>>();
        
        foreach (var str in strs)
        {
            string new_str = new string(str.OrderBy(x => x).ToArray());
            
            if (!dic.ContainsKey(new_str))
                dic.Add(new_str, new List<string>());
            
            dic[new_str].Add(str);
        }
        
        foreach (List<string> value in dic.Values)
            answer.Add(value);
        
        return answer;
    }
}

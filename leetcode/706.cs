/*
easy Design HashMap
url: https://leetcode.com/problems/design-hashmap/submissions/
후기: Dictionary 사용법 익히는 문제였다. 간단했다.
*/

public class MyHashMap {
    private Dictionary<int, int> dict;

    public MyHashMap() {
        dict = new Dictionary<int, int>();
    }
    
    public void Put(int key, int value) {
        if (!dict.ContainsKey(key)) dict.Add(key, value);
        else dict[key] = value;
    }
    
    public int Get(int key) {
        if (dict.ContainsKey(key)) return dict[key];
        else return -1;
    }
    
    public void Remove(int key) {
        if (dict.ContainsKey(key)) dict.Remove(key);
    }
}

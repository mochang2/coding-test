/*
medium Path Sum II
url: https://leetcode.com/problems/path-sum-ii/
후기: 개념은 어렵지 않았다. 다만 이유는 모르겠으나 28번째 줄에 new List로 해서 li_li에 추가해주지 않고, li_li.Add(li)만 하면
메모리를 공유해서 최종 결과에 빈 배열만 나오게 된다. 아마도 deep copy가 아니라 메모리만 공유하는 shallow copy인 것 같아.
이것 때문에 꽤나 시간이 오래 걸렸었다.
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public IList<IList<int>> li_li;
    
    public void Traverse(TreeNode node, int targetSum, int sum, List<int> li) {
        li.Add(node.val);
        if (node.left == null && node.right == null) {
            if (sum + node.val == targetSum) {
                Console.Write("\n");
                li_li.Add(new List<int>(li));
            }
        }
        else {
            if (node.left != null) Traverse(node.left, targetSum, sum + node.val, li);
            if (node.right != null) Traverse(node.right, targetSum, sum + node.val, li);
        }
        li.RemoveAt(li.Count - 1);
    }
    
    public IList<IList<int>> PathSum(TreeNode root, int targetSum) {
        if (root == null) return new List<IList<int>>();
        
        li_li = new List<IList<int>>();
        List<int> li = new List<int>();
        Traverse(root, targetSum, 0, li);
        
        return li_li;
    }
}

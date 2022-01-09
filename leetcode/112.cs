/*
easy Path Sum
url: https://leetcode.com/problems/path-sum/
후기: 생각보다 속도가 느렸다. 다른 풀이를 봐도 비슷했는데 함수를 하나 더 선언해서 공간복잡도는 높았다.
극단적으로 코드를 짧게 한 코드도 있었다. 이해는 잘 안되지만.
*/

// 내 풀이
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
    public int target;
    
    public bool Traverse(TreeNode node, int sum) {
        if (node.left == null && node.right == null) return sum + node.val == target;
        
        bool res1 = false;
        bool res2 = false;
        if (node.left != null) res1 = Traverse(node.left, sum + node.val);
        if (node.right != null) res2 = Traverse(node.right, sum + node.val);
        
        return res1 || res2;
    }
    
    public bool HasPathSum(TreeNode root, int targetSum) {
        target = targetSum;
        if (root != null) return Traverse(root, 0);
        return false;
    }
}


// 다른 사람 풀이
public bool HasPathSum(TreeNode root, int sum) {
    return root == null ? false :
           root.val == sum && root.left == null && root.right == null
        || HasPathSum(root.left, sum - root.val)
        || HasPathSum(root.right, sum - root.val);
}

/*
easy Maximum Depth of Binary Tree
url: https://leetcode.com/problems/maximum-depth-of-binary-tree/
후기: 144, 145 등에서 푼 tree traverse랑 매우 똑같아서 쉬웠다.
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
    public int max_depth;
    
    public void Traverse(TreeNode node, int temp) {
        if (node.left != null) Traverse(node.left, temp + 1);
        if (node.right != null) Traverse(node.right, temp + 1);
        max_depth = Math.Max(max_depth, temp);
    }
    
    public int MaxDepth(TreeNode root) {
        if(root == null) return 0;
        max_depth = 0;
        int temp = 0;
        Traverse(root, temp + 1);
        
        return max_depth;
    }
}

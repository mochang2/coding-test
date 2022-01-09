/*
easy Invert Binary Tree
url: https://leetcode.com/problems/invert-binary-tree/
후기: swap하는 문제였다. text editor가 없어서 swap이 되는지 몰라, 그냥 직접 구현했다.
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
    public void Traverse(TreeNode node) {
        TreeNode temp;
        temp = node.left;
        node.left = node.right;
        node.right = temp;
            
        if (node.left != null) Traverse(node.left);
        if (node.right != null) Traverse(node.right);
    }
    
    public TreeNode InvertTree(TreeNode root) {
        if (root != null) Traverse(root);
        return root;
    }
}

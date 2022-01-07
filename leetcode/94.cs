/*
easy Binary Tree Inorder Traversal
url: https://leetcode.com/problems/binary-tree-inorder-traversal/
후기: 144, 145랑 세트다.
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
    public List<int> list;
    
    public void Inorder(TreeNode node) {
        if (node.left != null) Inorder(node.left);
        list.Add(node.val);
        if (node.right != null) Inorder(node.right);
    }
    
    public IList<int> InorderTraversal(TreeNode root) {
        list = new List<int>();
        
        if (root != null) Inorder(root);
        
        return list;
    }
}

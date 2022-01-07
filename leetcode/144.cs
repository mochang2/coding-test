/*
easy Binary Tree Preorder Traversal
url: https://leetcode.com/problems/binary-tree-preorder-traversal/
후기: preorder이 뭐였는지 까먹었었다... bob 끝나고 CS 싹 다시 공부해야겠다.
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
    
    public void Preorder(TreeNode node) {
        list.Add(node.val);
        if (node.left != null) Preorder(node.left);
        if (node.right != null) Preorder(node.right);
    }
    
    public IList<int> PreorderTraversal(TreeNode root) {
        list = new List<int>();
        
        if (root != null) Preorder(root);
        
        return list;
    }
}

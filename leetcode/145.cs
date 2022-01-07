/*
easy Binary Tree Postorder Traversal
url: https://leetcode.com/problems/binary-tree-postorder-traversal/
후기: 144, 94랑 세트다.
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
    
    public void Postorder(TreeNode node) {
        if (node.left != null) Postorder(node.left);
        if (node.right != null) Postorder(node.right);
        list.Add(node.val);
    }
    
    public IList<int> PostorderTraversal(TreeNode root) {
        list = new List<int>();
        if (root != null) Postorder(root);
        return list;
    }
}

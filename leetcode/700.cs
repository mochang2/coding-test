/*
easy Search in a Binary Search Tree
url: https://leetcode.com/problems/search-in-a-binary-search-tree/
후기: tree를 하니까 확실히 재귀 감이 좋아진 것 같다. 어디서 return 해야할지 느낌이 왔다.
94, 101, 102, 104, 112, 144, 145, 226이 같은 트리 문제다.
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
    public TreeNode SearchBST(TreeNode node, int val) {
        if (node == null) return null;
        if (val == node.val) return node;
        
        if (node.left != null && val < node.val) return SearchBST(node.left, val);
        if (node.right != null && val > node.val) return SearchBST(node.right, val);
        
        return null;
    }
}

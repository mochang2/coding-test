/*
easy Lowest Common Ancestor of a Binary Search Tree
url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
후기: dfs(preorder)로 모든 leaf를 list에 넣어두고 common ancestor가 아닐 때까지 해당 list를 돌려서 다시 dfs를 하려고 했다.
말도 안되게 시간이 걸릴 것 같아 미리 답을 봤는데, 너무 깔끔한 답이라서 짜증났다. BST의 특징을 잘 파악하지 못한 것 같다.
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }  // unique value
 * }
 */

public class Solution {
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if ((root.val >= p.val && root.val <= q.val) || (root.val <= p.val && root.val >= q.val)) return root;
        else if (root.val >= p.val) return LowestCommonAncestor(root.left, p, q);
        else return LowestCommonAncestor(root.right, p, q);
    }
}

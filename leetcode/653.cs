/*
easy Two Sum IV - Input is a BST
url: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
후기: 완전탐색밖에 답이 없어서 li에 모든 node.val을 넣어놓고 이중 for문을 돌렸다.
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
    public List<int> li;
    
    public void traverse(TreeNode node) {
        li.Add(node.val);
        if (node.left != null) traverse(node.left);
        if (node.right != null) traverse(node.right);
    }
    
    public bool FindTarget(TreeNode root, int k) {
        li = new List<int>();
        traverse(root);
        for(int i = 0; i < li.Count - 1; i++) {
            for (int j = i + 1; j < li.Count; j++) {
                if (li[i] + li[j] == k) return true;
            }
        }
        
        return false;
    }
}

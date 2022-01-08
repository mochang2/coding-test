/*
easy Symmetric Tree
url: https://leetcode.com/problems/symmetric-tree/
후기: 못 풀어서 결국 답을 봤다. 재귀에는 여전히 약한 것 같다.
*/

// 첫 번째 시도
// // 반례 [1 2 2 2 null 2 null]
public class Solution {
    public List<int> left_tree;
    public List<int> right_tree;
    
    public void LeftTraverse(TreeNode node) {
        if (node.left != null) LeftTraverse(node.left);
        left_tree.Add(node.val);
        if (node.right != null) LeftTraverse(node.right);
    }
    
    public void RightTraverse(TreeNode node) {
        if (node.right != null) RightTraverse(node.right);
        right_tree.Add(node.val);
        if (node.left != null) RightTraverse(node.left);
    }
    
    public bool IsSymmetric(TreeNode root) {
        left_tree = new List<int>();
        right_tree = new List<int>();
        if (root.left != null) LeftTraverse(root.left);
        if (root.right != null) RightTraverse(root.right);
        
        if (left_tree.Count != right_tree.Count) return false;
        for (int i = 0; i < left_tree.Count; i++) {
            if (left_tree[i] != right_tree[i]) return false;
        }
        
        return true;
    }
}


// 두 번째 시도
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
    public bool Traverse(TreeNode node1, TreeNode node2) {
        if (node1 == null && node2 == null) return true;
        if (node1 == null || node2 == null) return false;
        if (node1.val != node2.val) return false;
        
        // if nodes are not null and nodes have the same value, traverse again
        return Traverse(node1.left, node2.right) && Traverse(node1.right, node2.left);
    }
    
    public bool IsSymmetric(TreeNode root) {
        // root != null
        return Traverse(root.left, root.right);
    }
}

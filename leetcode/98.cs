  /*
  medium Validate Binary Search Tree
  url: https://leetcode.com/problems/validate-binary-search-tree/
  후기:
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

// 첫 번째 시도 실패
// // 반례: [120,70,140,50,100,130,160,20,55,75,110,119,135,150,200]
// // 손자까지만 데이터를 주고 받는게 아니라, 해당 subtree에서의 최대, 최솟값까지 정보를 주고 받아야됨.
public class Solution {
    public bool Traverse(TreeNode node, TreeNode subroot) {
        if (node == null) return true;
        if (node.left != null && ((node.left.val >= node.val) || (subroot != null && subroot.right == node && node.left.val <= subroot.val))) {
            return false;
        }
        if (node.right != null && ((node.right.val <= node.val) || (subroot != null && subroot.left == node && node.right.val >= subroot.val))) {
            return false;
        }

        return Traverse(node.left, node) && Traverse(node.right, node);
    }

    public bool IsValidBST(TreeNode root) {
        return Traverse(root, null);
    }
}


// 두 번째 시도 성공
public class Solution {
    public bool IsValidBST(TreeNode root) {
        return traverse(root, long.MinValue, long.MaxValue);
    }

    private bool traverse(TreeNode node, long min, long max) {
        if (node == null) return true;
        if (min < node.val && node.val < max) return traverse(node.left, min, node.val) && traverse(node.right, node.val, max);

        return false;
    }
}

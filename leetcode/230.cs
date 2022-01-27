/*
medium Kth Smallest Element in a BST
url: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
후기: 27번째 줄에 postfix를 잘못 써서 answer이 계속 더해졌었다. && 조건의 순서를 바꾸니 해결됐다.
논리는 어렵지 않았으나 깔끔한 재귀는 아닌 것 같다.
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
    public int answer = 1;
    public bool found = false;
    
    public void Preorder(TreeNode node, int k) {
        if (found) return;
        if (node.left != null) Preorder(node.left, k);
        if (!found && answer++ == k) {
            answer = node.val;
            found = true;
            return ;
        }
        if (node.right != null) Preorder(node.right, k);
    }
    
    public int KthSmallest(TreeNode root, int k) {
        Preorder(root, k);
        return answer;
    }
}

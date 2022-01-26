/*
medium Binary Tree Right Side View
url: https://leetcode.com/problems/binary-tree-right-side-view/
후기: 오른쪽부터 preorder하면 됐다. BST인줄 알아서 다른 방법이 있는 줄 알고 고민했는데, 아니었다.
생각보다 간단한 문제였다.
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
    // 오른쪽부터 preorder하면 될 듯
    public List<int> answer;
    
    public void Traverse(TreeNode node, int depth) {
        if (node == null) return;
        else {
            if (answer.Count <= depth) {
                answer.Add(node.val);
            }
            Traverse(node.right, depth + 1);
            Traverse(node.left, depth + 1);
        }
    }
    
    public IList<int> RightSideView(TreeNode root) {
        answer = new List<int>();
        Traverse(root, 0);
        return answer;
    }
}

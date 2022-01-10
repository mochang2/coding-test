/*
medium Insert into a Binary Search Tree
url: https://leetcode.com/problems/insert-into-a-binary-search-tree/
후기: binary tree 문제에서 처음으로 생성자를 쓰는 문제였다.
input 중에서 tree가 아닌 input인지, 아님 내가 이해를 못 하는 input인지가 있어서 답을 봤다.
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
    public TreeNode InsertIntoBST(TreeNode node, int val) {
        if (node == null) return new TreeNode(val);
        else if (node.val > val) node.left = InsertIntoBST(node.left, val);
        else node.right = InsertIntoBST(node.right, val);
            
        return node;
    }
}

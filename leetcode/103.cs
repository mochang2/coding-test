/*
medium Binary Tree Zigzag Level Order Traversal
url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
후기: 102번 문제에서 많은 영감을 얻었다. 많이 틀렸지만, 감만 빨리 잡았으면 어렵진 않은 문제였을 것 같다.
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
    public IList<IList<int>> ZigzagLevelOrder(TreeNode root) {
        if (root == null) return new List<IList<int>>();
        
        IList<IList<int>> li_li = new List<IList<int>>();
        Queue<TreeNode> q = new Queue<TreeNode>();
        q.Enqueue(root);
        
        while (q.Count != 0) {
            int q_cnt = q.Count;
            int level = li_li.Count % 2;
            List<int> li = new List<int>();
            for (int i = 0; i < q_cnt; i++) {
                TreeNode first = q.Dequeue();
                li.Add(first.val);
                if (first.left != null) q.Enqueue(first.left);
                if (first.right != null) q.Enqueue(first.right);
            }
            if (level == 1) li.Reverse();
            li_li.Add(li);
        }
        
        
        return li_li;
    }
}

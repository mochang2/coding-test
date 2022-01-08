/*
medium Binary Tree Level Order Traversal
url: https://leetcode.com/problems/binary-tree-level-order-traversal/
후기: 각각의 스택 깊이마다 별도의 li를 가지고 있다가 해당 li에 node.val를 추가하는 식으로 코드를 짜려고 했으나
dfs 코드에서 어떤 위치에서 li를 생성해야할지 불규칙적이라 방법을 바꿨다.
대신 dfs를 depth라는 인자를 같이 줌으로써 해결했다.
알고리즘 속도가 너무 느려 다른 풀이를 봤는데 Queue를 쓰는 풀이가 훨씬 빨랐다. 아직 한참 부족하다.
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
// 내 풀이
public class Solution {
    public IList<IList<int>> li_li;
    
    public void Traverse(TreeNode node, int depth) {
        if (li_li.Count < depth + 1) {
            li_li.Add(new List<int>());
        }
        li_li[depth].Add(node.val);
        if (node.left != null) Traverse(node.left, depth + 1);
        if (node.right != null) Traverse(node.right, depth + 1);
    }
    
    public IList<IList<int>> LevelOrder(TreeNode root) {
        li_li = new List<IList<int>>();
        int depth = 0;
        if (root != null) Traverse(root, depth);
        
        return li_li;
    }
}


// Queue를 이용한 다른 사람 풀이(훨씬 빠름)
public class Solution {
    public IList<IList<int>> LevelOrder(TreeNode root) {
        var result = new List<IList<int>>();
        if (root == null) return result;

        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while (queue.Any()) {
            var size = queue.Count;
            var oneResult = new List<int>();
            for (int s = 0; s < size; s++) {
                var cur = queue.Dequeue();
                oneResult.Add(cur.val);

                if (cur.left != null) {
                    queue.Enqueue(cur.left);
                }

                if (cur.right != null) {
                    queue.Enqueue(cur.right);
                }
            }
            result.Add(oneResult);
        }

        return result;
    }
}

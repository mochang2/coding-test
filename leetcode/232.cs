/*
easy Implement Queue using Stacks
url: https://leetcode.com/problems/implement-queue-using-stacks/
후기: 2개의 stack을 통한 queue 구현. stack method를 익힐 수 있었다.
*/

public class MyQueue {
    public Stack<int> inStack;
    public Stack<int> outStack;

    public MyQueue() {
        inStack = new Stack<int>();
        outStack = new Stack<int>();
    }
    
    public void Push(int x) {
        while (outStack.Count != 0) {
            inStack.Push(outStack.Pop());
        }
        inStack.Push(x);
    }
    
    public int Pop() {
        while (inStack.Count != 0) {
            outStack.Push(inStack.Pop());
        }
        return outStack.Pop();
    }
    
    public int Peek() {
        while (inStack.Count != 0) {
            outStack.Push(inStack.Pop());
        }
        return outStack.Peek();
    }
    
    public bool Empty() {
        if (inStack.Count == 0 && outStack.Count == 0) 
            return true;
        return false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.Empty();
 */

/*
medium 3Sum
url: https://leetcode.com/problems/3sum/
후기: 처음에는 3중 for문을 생각했고, 비효율적이더라고 시간 안에 가능할 것 같아서 구현했더니 중복처리가 안 됐었다.
hashset으로 바꾸는 방법도 있지만 이왕 바꿀거 효율적인 코드로 바꾸려고 고민했다.
두 개의 포인터를 잡고 binary search하는 법을 찾으려고 했지만 건너뛰는 것도 많아질 것 같고 이 또한 중복처리에서 문제가 생길 것 같아 그냥 답을 봤다.
본 답은 한 점을 고정시키고 두 포인터 알고리즘을 하는 방법이었다.
*/


public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        // 정렬 이후 한 점을 고정
        // 투 포인터 알고리즘을 이용하여 총합이 0이 되는 지점을 찾음
        IList<IList<int>> answer = new List<IList<int>>();
        Array.Sort(nums, 0, nums.Length);  // -4 -1 -1 0 1 2
        
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] > 0) break;  // 오름차순으로 정렬했기 때문에 그 중에서 젤 작은 놈이 0보다 크면 break
            if (i > 0 && nums[i] == nums[i - 1]) continue;  // 겹치는 것을 answer에 넣지 않기 위한 코드1
            int start = i + 1;   // i를 기준으로 start와 end를 잡음
            int end = nums.Length - 1;
            
            while (start < end) { // 투 포인터 알고리즘
                if (nums[i] + nums[start] + nums[end] < 0) start++;
                else if (nums[i] + nums[start] + nums[end] > 0) end--;
                else {
                    answer.Add(new List<int>(new int[] { nums[i], nums[start], nums[end] }));
                    do {  // 겹치는 것을 answer에 넣지 않기 위한 코드2
                        start++;
                    } while(start < end && nums[start - 1] == nums[start]);
                    do {  // 겹치는 것을 answer에 넣지 않기 위한 코드3
                        end--;
                    } while(start < end && nums[end] == nums[end + 1]);
                }
            }
        }

        return answer;
    }
}

package LeetCode;

import java.util.HashMap;

class Solution_1 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i])) {
                map.put(target - nums[i], i);
            } else {
                return new int[]{i, map.get(nums[i])};
            }
        }
        return new int[]{0, 0};
    }
}
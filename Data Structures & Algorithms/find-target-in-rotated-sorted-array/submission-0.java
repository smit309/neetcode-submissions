class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int midpoint = left + (right - left) / 2;
            
            // If target found
            if (nums[midpoint] == target) {
                return midpoint;
            }
            
            // Determine if left half is sorted
            if (nums[left] <= nums[midpoint]) {
                // Check if target is in the left half
                if (nums[left] <= target && target < nums[midpoint]) {
                    right = midpoint - 1;
                } else {
                    left = midpoint + 1;
                }
            }
            // Otherwise, right half must be sorted
            else {
                // Check if target is in the right half
                if (nums[midpoint] < target && target <= nums[right]) {
                    left = midpoint + 1;
                } else {
                    right = midpoint - 1;
                }
            }
        }

        return -1;  // Target not found
    }
}

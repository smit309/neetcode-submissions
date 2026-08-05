class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        if(nums == null || nums.length < 3) return new ArrayList<>();
        Set<List<Integer>> output_arr = new HashSet<>();
        int n = nums.length;

        for(int i=0;i<n-2;i++){

            int left = i+1;
            int right = n-1;

            while(left < right){
                 int sum = nums[i] + nums[left] + nums[right];

                if(sum == 0){
                    output_arr.add(Arrays.asList(nums[i] ,nums[left] ,nums[right]));
                    left++;
                    right--;
                }
                else if(sum > 0){
                    right--;
                }
                else{
                    left++;
                }
            }
        }
        return new ArrayList<>(output_arr);
    
        
    }
}
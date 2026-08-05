class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer,Integer> hash_num = new HashMap<>();

        for(int i=0;i<nums.length;i++){
           int remainingSum = target - nums[i];

           if(hash_num.containsKey(remainingSum)){
                return new int[] {hash_num.get(remainingSum),i};

           }
           hash_num.put(nums[i],i);
        
            
        }
    throw new IllegalArgumentException("no found");
    }
}

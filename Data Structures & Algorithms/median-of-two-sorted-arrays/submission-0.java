class Solution {
    
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        // Combine both arrays using Stream.concat and convert back to int[]
        int[] result = Stream.concat(Arrays.stream(nums1).boxed(), Arrays.stream(nums2).boxed())
                      .mapToInt(Integer::intValue)
                      .toArray();
        
        // Sort the resulting array
        Arrays.sort(result);
        
        // Calculate the median
        int len = result.length;
        if (len % 2 == 0) {
            return (result[len / 2 - 1] + result[len / 2]) / 2.0;
        } else {
            return result[len / 2];
        }
    }
}

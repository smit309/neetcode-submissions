class Solution {
    public int maxArea(int[] heights) {
        
        int max_area = 0;
        int n = heights.length;

        int left_pointer = 0;
        int right_pointer = n-1;

        while(left_pointer<right_pointer){
            if(heights[left_pointer] < heights[right_pointer]){
                max_area = Math.max(max_area,heights[left_pointer] * (right_pointer-left_pointer));
                left_pointer++;
            }
            else{
                max_area = Math.max(max_area,heights[right_pointer] * (right_pointer-left_pointer));
                right_pointer--;

            }
        }
        return max_area;
    }
}

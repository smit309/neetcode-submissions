class Solution {
    public boolean hasDuplicate(int[] nums) {
        List<Integer> values = new ArrayList<>();

        for (int num : nums) {
            if (values.contains(num)) {
                return true; // Duplicate found
            }
            values.add(num); // Add the number to the list
        }

        return false; // No duplicates found
    }
}

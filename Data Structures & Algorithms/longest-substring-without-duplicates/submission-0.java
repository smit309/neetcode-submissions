class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left_pointer=0;
        int right_pointer = 0;

        int max = 0;
        HashSet<Character> hash_set = new HashSet<>();

        while(right_pointer < s.length()){
            if(!hash_set.contains(s.charAt(right_pointer))){
              hash_set.add(s.charAt(right_pointer));
              right_pointer++;
              max = Math.max(hash_set.size(),max);
            }
            else{
              hash_set.remove(s.charAt(left_pointer));
              left_pointer++;
            }
        }
        return max;
    }
}

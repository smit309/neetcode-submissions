class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase().replaceAll("[^a-z0-9]","");

        int n = s.length();
        int a_pointer = 0;
        int b_pointer = n-1;

        while(a_pointer <= b_pointer){
            if(s.charAt(a_pointer) != s.charAt(b_pointer)){
                return false;
            }
            a_pointer ++;
            b_pointer --;
        }
        return true;
    }
}

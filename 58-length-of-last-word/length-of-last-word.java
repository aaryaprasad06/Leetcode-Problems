class Solution {
    public int lengthOfLastWord(String s) {
        String array[]= s.split(" ");
        int len= array.length-1;
        int wordlen= array[len].length();
        return wordlen;
    }
}
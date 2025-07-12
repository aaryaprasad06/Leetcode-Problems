class Solution {
    public boolean isPalindrome(String s) {
        s= s.toLowerCase();
        String str="", rev="";
        for(int i=0; i<s.length(); i++)
        {
            char ch= s.charAt(i);
            if ( Character.isLetter(ch) || Character.isDigit(ch) )
            str= str + ch;
        }
        for(int i=str.length()-1; i>=0; i--)
        {
            rev= rev+ str.charAt(i);
        }
        if ( rev.equals(str) )
        return true;
        else
        return false;
    }
}
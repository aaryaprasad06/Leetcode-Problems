class Solution {
    public int getValue(char c)
    {
        int value;
        switch(c){
                case 'I': value=1; break;
                case 'V': value=5; break;
                case 'X': value=10; break;
                case 'L': value=50; break;
                case 'C': value=100; break;
                case 'D': value=500; break;
                case 'M': value=1000; break;
                default: value=0;
            }
            return value;
    }
    public int romanToInt(String s) {
        int sum=0, curr;
        int prev= getValue(s.charAt(0));
        for(int i=1; i< s.length(); i++)
        {
            curr= getValue(s.charAt(i));
            if (prev < curr)
            sum-=prev;
            else
            sum+=prev;
            prev=curr;
        }
        sum+=prev;
        return sum;
    }

    
}
class Solution {
    public boolean isUgly(int n) {
        if (n==1)
        return true;
        if( n<=0 )
        return false;
        int N=n;
        while ( N>1 )
        {
            if ( N%2 == 0)
            N/=2;
            else if ( N%3==0 )
            N/=3;
            else if ( N%5==0 )
            N/=5;
            else 
            return false;
        }
        return true;
    }
}
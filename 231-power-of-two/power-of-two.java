class Solution {
    public boolean isPowerOfTwo(int n) {
        if ( n<=0  )
        return false;
        if ( n==1 )
        return true;
        int N=n;
        while( N>1 )
        {
            if (N%2!=0)
            return false;
            N= N/2;
        }
        return true;
    }
}
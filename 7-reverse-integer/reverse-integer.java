class Solution {
    public int reverse(int x) {
        long rev=0;
        int a;
        while (x != 0)
        {
            a= x % 10;
            rev= (rev*10) + a;
            x= x / 10;
        }
        if (rev > Math.pow(2, 31)-1 || rev < Math.pow(-2, 31))
        return 0;
        else
        return (int)rev;
    }
}
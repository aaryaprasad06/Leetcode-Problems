class Solution {
    public boolean isHappy(int n) {
        int num=n;
        num= Add(num);
        while (num>1 && num!=4)
        {
            num= Add(num);
        }
        return (num==1)? true:false;
    }
    public int Add(int num){
        int sum=0, a;
        while (num>0)
        {
            a= num%10;
            sum= sum+ (a*a);
            num= num/10;
        }
        return sum;
    }
}
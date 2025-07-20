class Solution {
    public int missingNumber(int[] nums) {
        int ul= nums.length, found, i, j;
        for(i=0; i<=ul; i++)
        {
            found=0;
            for ( j=0; j<nums.length; j++)
            {
                if (nums[j]==i)
                {
                    found=1;
                    break;
                }
            }
            if(found==0)
            break;
        }
        return i;
    }
}
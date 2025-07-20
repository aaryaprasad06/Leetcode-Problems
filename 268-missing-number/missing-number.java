class Solution {
    public int missingNumber(int[] nums) {
        int ul=nums[0], found, i, j;
        for( i=0; i<nums.length; i++)
        {
            if(nums[i]>ul)
            ul= nums[i];
        }
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
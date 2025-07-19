class Solution {
    public void moveZeroes(int[] nums) {
        int ptr=0, l=nums.length, i=0;
        while (ptr<l && i<l)
        {
            if( nums[i]!=0)
            {
                nums[ptr]= nums[i];
                ptr++;
            }
            i++;
        }
        while(ptr<l)
        {
            nums[ptr++]=0;
        }
    }
}
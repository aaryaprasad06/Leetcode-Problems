class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length==0) 
        return 0;

        int k=1;
        for(int i=1; i< nums.length; i++)
        {
            if(nums[i]!=nums[i-1])
            nums[k++]= nums[i];
        }
        return k;
    }
    public int[] newArray(int[] nums)
    {
        int k= removeDuplicates(nums);
        int array[]= new int[k];
        for(int i=0; i<k; i++)
        {
            array[i]= nums[i];
        }
        return array;
    }
}
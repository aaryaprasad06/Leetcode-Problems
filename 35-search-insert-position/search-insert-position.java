class Solution {
    public int searchInsert(int[] nums, int target) {
        int ll=0, ul=nums.length-1, mid;
        while(ll<=ul)
        {
            mid= (ll+ul)/2;
            if( nums[mid]== target)
            return mid;
            else if  (nums[mid]<target)
            ll= mid+1;
            else
            ul= mid-1;
        }
        return ll;
    }
}
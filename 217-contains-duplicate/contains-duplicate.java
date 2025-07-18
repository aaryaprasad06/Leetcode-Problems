class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> hashmap= new HashMap<>();
        for(int i=0; i<nums.length; i++)
        {
            if(hashmap.containsKey(nums[i]))
            {
                int current=hashmap.get(nums[i]);
                hashmap.put(nums[i], current+1);
            }
            if (!hashmap.containsKey(nums[i]))
            {
                hashmap.put(nums[i], 1);
            }
        }
        for(int value:hashmap.values())
        {
            if(value>1)
            return true;
        }
        return false;
    }
}
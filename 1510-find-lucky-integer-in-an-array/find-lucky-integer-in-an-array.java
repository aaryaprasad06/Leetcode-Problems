class Solution {
    public int findLucky(int[] arr) {
        int count, index, n=arr.length;
        for(int i=0; i< n-1; i++)
        {
            for(int j=0; j<n-i-1; j++)
            {
                if(arr[j]>arr[j+1])
                {
                    int temp= arr[j];
                    arr[j]= arr[j+1];
                    arr[j+1]= temp;
                }
            }
        }
        for(int i=arr.length-1; i>=0; i--)
        {
            index= arr[i];
            count=0;
            for(int j=0; j<arr.length; j++)
            {
                if (arr[j]==index)
                count++;
            }
            if(count==index)
            return count;
        }
        return -1;
    }
}
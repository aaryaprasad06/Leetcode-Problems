class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            // If digit is less than 9, just increment and return
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            // Set current digit to 0 and continue to carry over
            digits[i] = 0;
        }

        // If all digits were 9 (e.g., [9,9,9] → [1,0,0,0])
        int[] result = new int[digits.length + 1];
        result[0] = 1;
        return result;
    }
}

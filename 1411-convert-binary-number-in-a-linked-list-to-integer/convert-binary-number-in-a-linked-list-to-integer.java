/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        String bin="";
        while(head!=null)
        {
            bin= bin + String.valueOf(head.val);
            head= head.next;
        }
        int num= Integer.parseInt(bin, 2);
        return num;
    }
}
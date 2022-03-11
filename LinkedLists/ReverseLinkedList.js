
  function ListNode(val, next) {
      this.val = (val===undefined ? 0 : val)
      this.next = (next===undefined ? null : next)
 }

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    return reverseListAcc(head, null);
};

/**
 * @param {ListNode} head
 * @param {ListNode} acc
 * @return {ListNode}
 */
function reverseListAcc(head, acc) {
    if(head == null) {
        return acc;
    }

    return reverseListAcc(head.next, new ListNode(head.val, acc));
}

function ListNode(val) {
	this.val = val;
	this.next = null;
}

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
	if (head == null) {
		return false;
	}

	let fast = head;
	let slow = head;

	while (fast != null) {
		fast = fast.next;

		if (fast == null) {
			return false;
		}

		fast = fast.next;
		slow = slow.next;

		if (fast == slow) {
			return true;
		}
	}

	return false;
};

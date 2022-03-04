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

	const seen = [];

	let curr = head;

	while (curr != null) {
		if (!seen.includes(curr)) {
			seen.push(curr);
		} else {
			return true;
		}

		curr = curr.next;
	}

	return false;
};

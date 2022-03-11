function ListNode(val, next) {
	this.val = val === undefined ? 0 : val;
	this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
	if (list1 == null) {
		return list2;
	} else if (list2 == null) {
		return list1;
	} else if (list1.val > list2.val) {
		return new ListNode(list2.val, mergeTwoLists(list1, list2.next));
	} else {
		return new ListNode(list1.val, mergeTwoLists(list1.next, list2));
	}
};

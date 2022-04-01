/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
	return binSearch(0, nums.length - 1, nums, target);
};

function binSearch(start, end, nums, target) {
	if (start > end) {
		return -1;
	}
	middle = start + Math.floor((end - start) / 2);
	midNum = nums[middle];

	if (midNum == target) {
		return middle;
	} else if (target > midNum) {
		return binSearch(middle + 1, end, nums, target);
	} else {
		return binSearch(start, middle - 1, nums, target);
	}
}

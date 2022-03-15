/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
	let len = nums.length;

	if (len < 2) {
		return nums[0];
	}

	let left = 0;
	let currSum = 0;
	let max = nums[0];

	for (let i = 0; i < k; i += 1) {
		currSum += nums[i];
	}

	max = currSum;

	for (let right = k; right < len; right += 1) {
		currSum += nums[right];
		currSum -= nums[left];

		if (currSum > max) {
			max = currSum;
		}

		left += 1;
	}

	return max / k;
};

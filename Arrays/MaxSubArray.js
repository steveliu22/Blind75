/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
	let length = nums.length;

	let leftIndex = 0;
	let prefixSum = nums[0];
	let maxSum = nums[0];

	for (let i = 1; i < length; i += 1) {
		if (prefixSum < 0) {
			leftIndex = i;
			prefixSum = nums[i];
		} else {
			prefixSum += nums[i];
		}

		if (prefixSum > maxSum) {
			maxSum = prefixSum;
		}
	}

	return maxSum;
};

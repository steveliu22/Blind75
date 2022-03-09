/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
	let len = nums.length;

	if (len == 1) {
		return nums[0];
	} else {
		let max = nums[0];
		let prefixSum = nums[0];
		let left = 0;

		for (let i = 1; i < len; i += 1) {
			if (prefixSum < 0) {
				left = i;
				prefixSum = nums[i];
				continue;
			}

			let sum = prefixSum + nums[i];
			prefixSum += nums[i];

			if (sum > max) {
				max = sum;
			}
		}

		let maxNumInNums = Math.max(...nums);

		return max > maxNumInNums ? max : maxNumInNums;
	}
};

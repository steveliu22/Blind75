/**
 * @param {number[]} nums
 * @return {number}
 */

//utilizes the sliding window pattern
var maxSubArray = function (nums) {
	let length = nums.length;

	let leftIndex = 0;
	let prefixSum = nums[0]; // we are keeping track of the sum that we've accumulated so far in our sub array
	let maxSum = nums[0];

	for (let i = 1; i < length; i += 1) {
		//if the sum we've accumulated so far is negative, then it will only decrease the value of our sub array
		//so we have to get rid of all of the numbers from leftIndex to i - 1 and start over with a new sub array so
		//we then slide the left most point to our current index
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

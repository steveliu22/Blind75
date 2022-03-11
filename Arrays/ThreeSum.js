/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const length = nums.length;

    if(length < 3) {
        return [];
    }

    const sorted = nums.sort(function(a, b) {return a - b});
    const seen = [];
    const ans = [];
    
    for(let i  = 0; i < nums.length - 2; i += 1) {

        let currNum = sorted[i];
    
        if(i > 0 && sorted[i] == sorted[i - 1]) {
            continue;
        }

        let leftPointer = i + 1;
        let rightPointer = length - 1;
        let target = -1 * currNum;
        
        while(leftPointer != rightPointer) {
           let sum = sorted[leftPointer] + sorted[rightPointer];
           if(sum > target) {
                rightPointer = rightPointer - 1;
            }

            else if (sum < target) {
                leftPointer = leftPointer + 1;
            }

            else {
                
                ans.push([currNum, sorted[leftPointer], sorted[rightPointer]]);

                while(sorted[leftPointer] == sorted[leftPointer + 1]) {
                    leftPointer += 1;
                }

                
                while(sorted[rightPointer] == sorted[rightPointer - 1]) {
                    rightPointer -= 1;
                }

                leftPointer += 1;
                rightPointer -= 1;
            }

        }

        seen.push(currNum);

    }

    return ans;
}


console.log(threeSum([-1,0,1,2,-1,-4]));

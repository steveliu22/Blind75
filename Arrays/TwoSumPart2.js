/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let length = numbers.length;
    let pointer1 = 0;
    let pointer2 = length - 1;
    let ans = numbers[pointer1] + numbers[pointer2];

    while(ans != target) {
        
        if(ans > target) {
            pointer2 = pointer2 - 1;
        }

        else if(ans < target) {
            pointer1 = pointer1 + 1;
        }

        ans = numbers[pointer1] + numbers[pointer2];
    }

    return [pointer1 + 1, pointer2 + 1];
};
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
	alphanumeric = s.replace(/[^0-9a-z]/gi, "");

	lower = alphanumeric.toLowerCase();

	pointer1 = 0;
	pointer2 = lower.length - 1;

	while (pointer2 > pointer1) {
		p1 = lower[pointer1];
		p2 = lower[pointer2];
		if (p1 != p2) {
			return false;
		}

		pointer1 += 1;
		pointer2 -= 1;
	}

	return true;
};

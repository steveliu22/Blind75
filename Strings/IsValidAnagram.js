/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
	dict1 = {};
	dict2 = {};

	[...s].forEach((element) => {
		if (element in dict1) {
			dict1[element] = dict1[element] + 1;
		} else {
			dict1[element] = 1;
		}
	});

	[...t].forEach((element) => {
		if (element in dict2) {
			dict2[element] = dict2[element] + 1;
		} else {
			dict2[element] = 1;
		}
	});

	let ans = true;
	let iterate = dict1;

	if (s.length < t.length) {
		iterate = dict2;
	}

	Object.keys(iterate).forEach((elem) => {
		if (!(elem in dict2)) {
			ans = false;
			return;
		} else {
			if (dict2[elem] != dict1[elem]) {
				ans = false;
				return;
			}
		}
	});

	return ans;
};

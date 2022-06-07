/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, newColor) {
	const oldColor = image[sr][sc];

	return floodFillHelp(image, sr, sc, newColor, oldColor, 0);
};

function floodFillHelp(image, sr, sc, newColor, originalColor, calls) {
	if (calls > image.length * image[0].length) {
		return image;
	}

	const fills = existsAtleastOneNeighbor(image, sr, sc, originalColor);
	const len = fills.length;
	image[sr][sc] = newColor;
	if (len == 0) {
		return image;
	} else {
		fills.forEach((coordinate) => {
			let i = coordinate[0];
			let j = coordinate[1];
			image[i][j] = newColor;
			floodFillHelp(image, i, j, newColor, originalColor, calls + 1);
		});

		return image;
	}
}

function existsAtleastOneNeighbor(image, sr, sc, oldColor) {
	let left = sc - 1;
	let right = sc + 1;
	let top = sr - 1;
	let bot = sr + 1;
	let height = image.length;
	let width = image[0].length;

	const fillCoordinates = [];

	if (left >= 0 && image[sr][left] == oldColor) {
		fillCoordinates.push([sr, left]);
	}
	if (right < width && image[sr][right] == oldColor) {
		fillCoordinates.push([sr, right]);
	}
	if (bot < height && image[bot][sc] == oldColor) {
		fillCoordinates.push([bot, sc]);
	}
	if (top >= 0 && image[top][sc] == oldColor) {
		fillCoordinates.push([top, sc]);
	}

	return fillCoordinates;
}

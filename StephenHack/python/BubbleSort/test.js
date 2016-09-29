function remove(arr, start, end) {
	for (var i = 0; i < arr.length - 1 - end; i++){
		arr[i + start] = arr[i + end + 1];
	}
	for (var n=0; n< end - start + 1; n++){
		arr.pop();
	}
	return arr;
}

console.log (remove([1,4,5,4,3], 1, 3))
function zipIt(arr1, arr2){
	var arr3 = [];
	if (arr1.length <= arr2.length) {
		for (var i = 0; i < arr1.length; i++){
			arr3.push(arr1[i]);
			arr3.push(arr2[i]);
		}
		for (var j = arr1.length; j < arr2.length; j++){
			arr3.push(arr2[j]);
		}
	}
	else {
		for (var i = 0; i < arr2.length; i++){
			arr3.push(arr1[i]);
			arr3.push(arr2[i]);
		}
		for (var j = arr2.length; j < arr1.length; j++){
			arr3.push(arr1[j]);
		}
	}
	return arr3;
}
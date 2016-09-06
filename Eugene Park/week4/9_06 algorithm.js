function secondLargest(arr) {
	if(arr.length < 2)
		return null;
	else {
		for(var i = 1; i < arr.length; i++){
			if(arr[i-1] < arr [i]){
				var temp = arr[i-1];
				arr[i-1] = arr[i];
				arr[i] = temp;
				i = 0;
				// console.log(arr);
			}
		}
		return arr[1];
	}
}
console.log(secondLargest([5,6,2,8,1,9]));
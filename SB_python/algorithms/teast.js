function shuffle(arr) {
	for (var i = 0; i < arr.length; i++) {
		roll = Math.floor(Math.random() * arr.length)
		temp = arr[i]
		arr[i] = arr[roll]
		arr[roll] = temp
	}
	return arr
}

console.log(shuffle([1,2,3,4,5,6,7]))
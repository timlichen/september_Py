function db(arr){
	for (var i =0; i < arr.length; i +=2){
		for (var j = arr.length-1 ; j >= i ; j--){
			arr[j+1] = arr[j];
		}
	}
	return arr;
}

function remove_range(arr,start,end){
	for(var i =0; i < arr.length-1-end; i++){
		arr[i+start] = arr[i+end+1];
	}
	for(var n=0; n < end-start+1; n++){
		arr.pop();
	}
	return arr;
}

function shuffle(arr){
	for(var i=0; i <arr.length; i++){
		roll = Math.floor(Math.random()*arr.length);
		temp = arr[i];
		arr[i] = arr[roll];
		arr[roll] = temp;
	}
	return arr;
}

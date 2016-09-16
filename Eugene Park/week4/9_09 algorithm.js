function removeBlanks(string1){
	var arr = string1.split(" ");
	return arr.join("");
}

function acronyms(string1){
	string1 = string1.toUpperCase();
	var arr = string1.split(" ");
	var acr = '';
	for(var i=0; i<arr.length; i++){
		acr += arr[i][0];
	}
	return acr;
}

function removeShorterStrings(arr, slen){
	for(var i=0; i<arr.length; i++){
		if(arr[i].length < slen){
			for(var j=i; j<arr.length-1; j++){
				arr[j] = arr[j+1];
			}
			arr.pop();
		}
	}
	return arr;
}
console.log(removeBlanks("Pl     ayTha tF u nkyM    usi    c  "));
console.log(acronyms("Fucked up beyond all recognition"));
console.log(removeShorterStrings(['longing', 'rusted', 'seventeen', 'daybreak', 'furnace', 'nine', 'penign', 'homecoming', 'one', 'freigth car'], 5));
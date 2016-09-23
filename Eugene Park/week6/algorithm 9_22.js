function ListNode(value){
	this.val = value;
	this.next =null;
}

function SListSecondLargest(){
	this.head = null;
	this.secondLargest = function(LN){
		node = this.head
		var max = this.head.val;
		while(node){
			if(node.val > max){
				max = node.val;
			}
			node = node.next;
		}
		node = this.head;
		if(max == node.val){
			var sndmax = node.next.val;
		}
		else{
			var sndmax = node.val;
		}
		while(node){
			if(node.val > sndmax && node.val < max){
				sndmax = node.val;
			}
			node = node.next;
		}
		return sndmax;
	}
}

function DedupeSlist(LN){
	var values = [];
	prev = this.head;
	node = this.head.next;
	values.push(this.head.val)
	while(node){
		var dupe = false;
		for(var i = 0; i < values.length; i++){
			if(values[i]==node.val){
				dupe = true;
			}
		}
		if(dupe){
			prev.next = node.next;
			node = node.next;
		}
		else{
			values.push(node.val);
			prev = prev.next
			node = node.next
		}
	}
	return this;
}

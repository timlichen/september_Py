function SLList(node) {
	this.head = node
	this.addFront = function(value) {
		first = new Node(value)
		first.next = this.head
		this.head = first
		return first
	}
	this.remFront = function() {
		if (this.head) {
			this.head = this.head.next
			return this.head
		} else {
			return null
		}
	}
	this.contains = function(LN, val) {
		while (LN) {
			if (LN.val == val) {
				return LN
			}
			LN = LN.next
		}
		return false
	}
	this.front = function(LN) {
		if (LN) {
			return LN.val
		} else {
			return null
		}
	}
}

function Node(val) {
	this.val = val
	this.next = null
}
node1 = new Node(2)
SL = new SLList(new Node(5));
console.log(SL)
SL.addFront(3)
console.log(SL)
SL.addFront(1)
console.log(SL)
SL.remFront()
console.log(SL)
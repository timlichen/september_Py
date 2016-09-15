import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        self._ = Underscore()
        self.test_list = [1,2,3,4,5]
        self.mapresult = self._.map(self.test_list, lambda x: x * 2)
        self.test_list = [1,2,3,4,5]
        self.reduceresult = self._.reduce(self.test_list, lambda memo, e: memo + e, 0)
        self.test_list = [1,2,3,4,5]
        self.findresult = self._.find(self.test_list, lambda x: x % 2 == 0)
        self.test_list = [1,2,3,4,5]
        self.filterresult = self._.filter(self.test_list, lambda x: x % 2 == 0)
        self.test_list = [1,2,3,4,5]
        self.rejectresult = self._.reject(self.test_list, lambda x: x % 2 == 0)
    def testMap(self):
    	return self.assertEqual([2,4,6,8,10], self.mapresult)
    def testReduce(self):
        return self.assertEqual(15, self.reduceresult)
    def testFind(self):
        return self.assertEqual(2, self.findresult)
    def testFilter(self):
        return self.assertEqual([2,4], self.filterresult)
    def testReject(self):
        return self.assertEqual([1,3,5], self.rejectresult)

if __name__ == "__main__":
    unittest.main()
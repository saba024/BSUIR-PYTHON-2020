import unittest
import sort
import cached
import vector
import Formjson

class SortingTest(unittest.TestCase):
	def find_if_file_can_be_sorted(self):
		with open('digit.txt', 'w') as file:
			file.writelines('{}\n'.format(random.randint(1,1000000)) for _ in range(int(100)))

		with self.assertRaises(Exception):
			sort.splitFiles("digit.txt",10)
			sort.mergeSortedtemplefiles()

	def test_sort(self):
		list1 = [17,1,19,5,6,23,11]
		list2 = list1
		sort.externamMergeSort().mergeSort(list2)
		self.assertEqual(list2,sorted(list1))


class CachedTest(unittest.TestCase):
	def test_right_answer(self):
		self.assertEqual(int(cached.add(5, 10)), 15)

	def test_right_answer(self):
		self.assertEqual(int(cached.plusandpow(3, 2, 3)), 125)	
		



class JSONtext(unittest.TestCase):
	def text_is_str(self):
		self.assertTrue(Formjson.converttodict("admin",19,["Jane","John"], 345.80, ["Doe","Joe"],True, None), str)

	def test_donot_support(self):
		with self.assertRaises(TypeError):
			user = Formjson.User("admin",19)
			
		

class Vectortest(unittest.TestCase):
	def test_plus(self):
		self.assertEqual(vector.Vector([1,2,2],3).countlen(),3)

	def test_plus_not_vector(self):
		with self.assertRaises(TypeError):
			print(vector.Vector([5,5],2) + 5)	

	
unittest.main()		
		

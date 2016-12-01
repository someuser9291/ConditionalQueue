import unittest

from LinkedList import LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.__list = LinkedList()

    def test_append(self):
        self.__list.append(1)
        self.assertEqual(1, len(self.__list))

    def test_insert(self):
        self.__list.insert(0, 1)
        self.__list.insert(0, 1738)

        self.assertEqual(1738, self.__list[0])
        self.assertEqual(2, len(self.__list))

    def test_remove(self):
        self.__list.append(1)
        self.assertEqual(1, self.__list[0])

        self.__list.remove(1)
        self.assertEqual(0, len(self.__list))

    def test_pop(self):
        self.__list.append(1)
        self.__list.append(2)
        self.__list.append(3)

        self.__list.remove(2)

        self.assertEqual(3, self.__list[1])

    def test_negative_index(self):
        self.__list.append(1)
        self.__list.append(2)
        self.__list.append(3)

        self.assertEqual(3, self.__list[-1])
        self.assertEqual(2, self.__list[-2])
        self.assertEqual(1, self.__list[-3])

    def test_set_item(self):
        self.__list.append(1)
        self.__list[0] = 2
        self.assertEqual(2, self.__list[0])

    def test_iteration(self):
        for i in xrange(10):
            self.__list.append(i)

        for index, item in enumerate(self.__list):
            self.assertEqual(item, self.__list[index])

    def test_reverse(self):
        self.__list.append(1)
        self.__list.append(2)
        self.__list.append(3)

        self.assertEqual(1, self.__list[0])

        self.__list.reverse()

        self.assertEqual(3, self.__list[0])


    def test_sort(self):
        self.__list.append(3)
        self.__list.append(1)
        self.__list.append(2)

        self.assertEqual(3, self.__list[0])

        self.__list.sort()

        for i in xrange(1, 4):
            self.assertEqual(i, self.__list[i - 1])


if __name__ == "__main__":
    unittest.main()

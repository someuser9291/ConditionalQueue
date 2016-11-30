import unittest
import time
from threading import Thread


from Queue import Empty
from ConditionalQueue import ConditionalQueue


class ConditionalQueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = ConditionalQueue()
        for i in xrange(10):
            self.queue.put(i)

    def test_regular_queue_usage(self):
        old_size = self.queue.qsize()
        self.queue.put(11)
        self.assertEqual(old_size + 1, self.queue.qsize())

        self.assertEqual(0, self.queue.get())
        self.assertEqual(old_size, self.queue.qsize())

        for i in xrange(self.queue.qsize()):
            self.queue.get()

        self.assertEqual(0, self.queue.qsize())

        with self.assertRaises(Empty):
            self.queue.get(block=False)

        with self.assertRaises(Empty):
            self.queue.get(block=True, timeout=0.1)

    def test_conditional_functionality(self):
        item = self.queue.get(condition_lambda=lambda item: item == 5)
        self.assertEqual(5, item)

        with self.assertRaises(Empty):
            self.queue.get(block=False, condition_lambda=lambda item: item == 5)

        with self.assertRaises(Empty):
            self.queue.get(block=True, timeout=0.1, condition_lambda=lambda item: item == 5)

    def test_thread_safety(self):
        def consumer(allowed_number):
            item = self.queue.get(block=True, condition_lambda=lambda item: item==allowed_number)
            self.assertEqual(allowed_number, item)

        threads = []
        for i in xrange(10):
            t = Thread(target=consumer, args=(i,))
            t.start()
            threads.append(t)

        start_time = time.time()

        # Producer
        for i in xrange(len(threads)):
            self.queue.put(i)
            # Minor sleeps to let the consumers block
            time.sleep(0.2)

        for thread in threads:
            thread.join()

        self.assertLessEqual(time.time() - start_time, 0.2 * len(threads) * 1.1)


if __name__ == "__main__":
    unittest.main()

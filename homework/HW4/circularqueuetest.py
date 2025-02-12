import unittest
from process import Process
from circularqueue import CircularQueue

class TestCircularQueue(unittest.TestCase):

    def setUp(self):
        """Prepare a basic setup for tests."""
        self.p1 = Process(pid=1, cycles=5)
        self.p2 = Process(pid=2, cycles=3)
        self.p3 = Process(pid=3, cycles=2)
        self.p4 = Process(pid=4, cycles=4)
        
    # Test init with empty queue
    def test_init_empty(self):
        cq = CircularQueue()
        self.assertEqual(len(cq), 0)
        self.assertEqual(repr(cq), "There are 0 items in queue")

    # Test init with a list of processes
    def test_init_with_processes(self):
        cq = CircularQueue([self.p1, self.p2, self.p3])
        self.assertEqual(len(cq), 3)
        self.assertEqual(repr(cq), "There are 3 items in queue")

    # Test add_process (add one process to empty queue)
    def test_add_process_to_empty(self):
        cq = CircularQueue()
        cq.add_process(self.p1)
        self.assertEqual(len(cq), 1)
        self.assertEqual(repr(cq), "There are 1 items in queue")

    # Test add_process (add two processes to empty queue)
    def test_add_two_processes_to_empty(self):
        cq = CircularQueue()
        cq.add_process(self.p1)
        cq.add_process(self.p2)
        self.assertEqual(len(cq), 2)
        self.assertEqual(repr(cq), "There are 2 items in queue")

    # Test add_process (add three processes to empty queue)
    def test_add_three_processes_to_empty(self):
        cq = CircularQueue()
        cq.add_process(self.p1)
        cq.add_process(self.p2)
        cq.add_process(self.p3)
        self.assertEqual(len(cq), 3)
        self.assertEqual(repr(cq), "There are 3 items in queue")

    # Test repr (check the correct string for a queue of 3 processes)
    def test_repr_for_three_processes(self):
        cq = CircularQueue([self.p1, self.p2, self.p3])
        self.assertEqual(repr(cq), "There are 3 items in queue")

    # Test remove_process (remove from middle of CQ with 3 processes)
    def test_remove_process_from_middle(self):
        cq = CircularQueue([self.p1, self.p2, self.p3])
        cq.remove_process(self.p2)
        self.assertEqual(len(cq), 2)
        self.assertEqual(repr(cq), "There are 2 items in queue")

    # Test remove_process (remove from front of CQ with 3 processes)
    def test_remove_process_from_front(self):
        cq = CircularQueue([self.p1, self.p2, self.p3])
        cq.remove_process(self.p1)
        self.assertEqual(len(cq), 2)
        self.assertEqual(repr(cq), "There are 2 items in queue")

    # Test remove_process (remove from end of CQ with 3 processes)
    def test_remove_process_from_end(self):
        cq = CircularQueue([self.p1, self.p2, self.p3])
        cq.remove_process(self.p3)
        self.assertEqual(len(cq), 2)
        self.assertEqual(repr(cq), "There are 2 items in queue")

    # Test remove_process (remove the only process in CQ)
    def test_remove_process_from_single_item(self):
        cq = CircularQueue([self.p1])
        cq.remove_process(self.p1)
        self.assertEqual(len(cq), 0)
        self.assertEqual(repr(cq), "There are 0 items in queue")

    # Test kill (kill process in middle of CQ with 3 processes)
    def test_kill_process_middle(self):
        cq = CircularQueue([self.p1, self.p2, self.p3])
        killed_process = cq.kill(self.p2)
        self.assertEqual(killed_process, self.p2)
        self.assertEqual(len(cq), 2)
        self.assertEqual(repr(cq), "There are 2 items in queue")

if __name__ == '__main__':
    unittest.main()

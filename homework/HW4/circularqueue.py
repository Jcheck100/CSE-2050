from process import Process


class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn"""

    def __init__(self, processes=None):
        self._head = None
        self._len = 0
        self._d_processes = {}

        if processes:
            for i in processes:
                self.add_process(i)

    def __len__(self):

        return self._len

    def __repr__(self):
        """Tells how many items are in teh queue

        Returns:
            str: how many items are in queue
        """
        return f"There are {self._len} items in queue"

    def add_process(self, process):
        """Adds a process to the CircularQueue.

        Args:
            process (Process): The process to be added to the queue
        """
        if self._head == None:
            self._head = process
            process.link = process
            process.prev = process
        else:
            last_process = self._head.prev
            last_process.link = process
            process.prev = last_process
            process.link = self._head
            self._head.prev = process
        self._len += 1
        self._d_processes[process.pid] = process

    def kill(self, process):
        self._d_processes.pop(process.pid)

        self.remove_process(process)
        return process

    def remove_process(self, process):
        """Removes a process from the CircularQueue.

        Args:
            process (Process): The process to be removed from the queue.

        Returns:
            Process: The process that was removed from the queue.

        Raises:
            ValueError: If the queue is empty, an exception is raised when trying
                        to remove a process.
        """
        if self._head is None:
            raise ValueError("Cannot remove a process from an empty queue.")

        if self._len == 1:
            self._head = None
        else:
            last_process = process.prev
            next_process = process.link

            last_process.link = next_process
            next_process.link = last_process

            if self._head == process:
                self._head = next_process
        self._len -= 1
        return process

    def run(self, n_cycles):
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time"""
        n_remaining = n_cycles
        return_strings = (
            []
        )  # Using an intermediate list since appending to a string is O(n)

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(
                    f"{self._head.pid} finished after {n_cycles-n_remaining+1} computational cycles."
                )
                self.remove_process(self._head)

            else:
                self._head = self._head.link

            n_remaining -= 1

        return "\n".join(return_strings)

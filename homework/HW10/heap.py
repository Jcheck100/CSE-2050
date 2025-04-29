from entry import Entry


class Heap:
    def __init__(self):
        """
        Initializes an empty min-heap.
        """
        self._L = []
        self._idx = {}

    def __len__(self):
        """
        Returns the number of entries in the heap.
        """
        return len(self._L)

    def __iter__(self):
        """
        Iterates over the heap by repeatedly yielding the minimum element.
        """
        while self._L:
            yield self.remove_min()

    def idx_parent(self, idx):
        """
        Returns the index of the parent of the given node, or None if root.
        """
        if idx == 0:
            return None
        else:
            return (idx - 1) // 2

    def idx_left(self, idx):
        """
        Returns the index of the left child of the given node, or None if out of bounds.
        """
        left = 2 * idx + 1
        if left >= len(self._L):
            return None
        return left

    def idx_right(self, idx):
        """
        Returns the index of the right child of the given node, or None if no children.
        """
        right = 2 * idx + 2
        if right >= len(self._L):
            return None
        return right

    def idx_min_child(self, idx):
        """
        Returns the index of the child with the smallest priority, or None if no children.
        """
        left = self.idx_left(idx)
        right = self.idx_right(idx)
        if left is None:
            return None
        if right is None:
            return left

        if self._L[left] <= self._L[right]:
            return left
        else:
            return right

    def insert(self, item, priority):
        """
        Inserts a new item into the heap with the given priority.
        """
        entry = Entry(item, priority)
        self._L.append(entry)
        idx = len(self._L) - 1
        self._idx[item] = idx
        self._upheap(idx)

    def remove_min(self):
        """
        Removes and returns the entry with the smallest priority.
        """
        if not self._L:
            return None
        min = self._L[0]
        last = self._L.pop()
        if self._L:
            self._L[0] = last
            self._idx[last.item] = 0
            self._downheap(0)

        del self._idx[min.item]
        return min

    def change_priority(self, item, priority):
        """
        Changes the priority of an existing item and reorders the heap.
        Returns the new index of the item.
        """

        idx = self._idx[item]
        entry = self._L[idx]
        old_priority = entry.priority
        entry.priority = priority

        if priority < old_priority:
            self._upheap(idx)
        else:
            self._downheap(idx)

        return self._idx[item]

    def _swap(self, i, j):
        """
        Swaps entries at indices i and j and updates the index map.
        """
        self._L[i], self._L[j] = self._L[j], self._L[i]
        self._idx[self._L[i].item] = i
        self._idx[self._L[j].item] = j

    def _upheap(self, idx):
        """
        Bubbles the entry at idx up to restore heap order.
        """
        parent = self.idx_parent(idx)

        while parent is not None and self._L[idx] < self._L[parent]:
            self._swap(idx, parent)
            idx = parent
            parent = self.idx_parent(idx)

    def _downheap(self, idx):
        """
        Pushes the entry at idx down to restore heap order.
        """
        min_child = self.idx_min_child(idx)
        while min_child is not None and self._L[idx] > self._L[min_child]:
            self._swap(idx, min_child)
            idx = min_child
            min_child = self.idx_min_child(idx)

    @staticmethod
    def heapify(entries):
        """
        Builds a min-heap from a list of Entry objects and returns a Heap instance.
        """
        heap = Heap()
        heap._L = entries
        heap._idx = {entry.item: i for i, entry in enumerate(entries)}

        for i in reversed(range(len(entries) // 2)):
            heap._downheap(i)
        return heap

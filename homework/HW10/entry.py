class Entry:
    def __init__(self, item, priority):
        """
        Initializes an entry with an item and its associated priority.
        """
        self.priority = priority
        self.item = item

    def __eq__(self, other):
        """
        Returns True if priorities are equal.
        """
        return self.priority == other.priority

    def __lt__(self, other):
        """
        Returns True if this entry has a lower priority than the other.
        """
        return self.priority < other.priority

    def __le__(self, other):
        """
        Returns True if this entry has lower or equal priority than the other.
        """
        return self.priority <= other.priority

    def __repr__(self):
        """
        Returns a string representation of the entry.
        """
        return f"Entry(item={self.item}, priority={self.priority})"

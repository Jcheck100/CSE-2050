class LocalRecord:
    def __init__(self, pos, max=None, min=None):
        """
        Initialize a LocalRecord object with a rounded position and optional initial min/max temperatures
        """
        self.pos = (round(pos[0], 0), round(pos[1], 0))
        self.max = max
        self.min = min

    def add_report(self, temp):
        """
        Add a temperature report to the record, updating min and max as needed
        """
        if self.max is None or temp > self.max:
            self.max = temp
        if self.min is None or temp < self.min:
            self.min = temp

    def __eq__(self, other):
        """
        Check equality based on rounded position
        """
        return isinstance(other, LocalRecord) and self.pos == other.pos

    def __hash__(self):
        """
        Calculate hash based on position.
        """
        return hash(self.pos)

    def __repr__(self):
        """
        Return a string representation of the record
        """
        return f"Position: {self.pos}, Max: {self.max}, Min: {self.min}"


class RecordsMap:
    def __init__(self):
        """
        Initialize the RecordsMap with default bucket size and counters
        """
        self.size = 8
        self.count = 0
        self.buckets = [[] for _ in range(self.size)]

    def __len__(self):
        """
        Return the number of unique positions in the map
        """
        return self.count

    def _bucket_index(self, pos):
        """
        Calculate the index of the bucket at given position
        """
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))
        return hash(rounded_pos) % self.size

    def add_report(self, pos, temp):
        """
        Add a temperature report for a specific position
        If position already exists, updates the record @ that position
        """
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))
        idx = self._bucket_index(pos)
        bucket = self.buckets[idx]

        for record in bucket:
            if record.pos == rounded_pos:
                record.add_report(temp)
                return

        new_record = LocalRecord(pos)
        new_record.add_report(temp)
        bucket.append(new_record)
        self.count += 1

        if self.count / self.size > 0.75:
            self._rehash(self.size * 2)

    def __getitem__(self, pos):
        """
        Get the min and max temperatures recorded at a given position
        """
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))
        idx = self._bucket_index(pos)
        bucket = self.buckets[idx]
        for record in bucket:
            if record.pos == rounded_pos:
                return (record.min, record.max)
        raise KeyError

    def __contains__(self, pos):
        """
        Checks if a position exists in the map
        """
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))
        idx = self._bucket_index(pos)
        bucket = self.buckets[idx]
        for record in bucket:
            if record.pos == rounded_pos:
                return True
        return False

    def _rehash(self, new_size):
        """
        Resize the bucket array and re-insert all existing records
        """
        old_buckets = self.buckets
        self.size = new_size
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_buckets:
            for record in bucket:
                self.add_report(record.pos, record.max)
                if record.min != record.max:
                    self.add_report(record.pos, record.min)

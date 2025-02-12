class Process:
    def __init__(self, pid, cycles = 100):
        self.pid = pid
        self.cycles = cycles
        self.link = None
        self.prev = None

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.pid == other.pid
        return False

    def __repr__(self):
        return f"{self.pid} {self.cycles}"


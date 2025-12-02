class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __str__(self):
        s = '['
        s += str(self.priority)
        s += ' | '
        s += str(self.description)
        s += ']'
        return s

    def __gt__(self, other):
        return self.priority > other.priority

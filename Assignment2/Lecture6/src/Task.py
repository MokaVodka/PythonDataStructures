class Task:
    def __init__(self, priority, description):
        if priority is None or type(priority) is not int:
            raise ValueError('Priority must be an int')
        if description is None or type(description) is not str:
            raise ValueError('Description must be an string')

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
        if other is None or type(other) is not Task:
            raise ValueError('Task can only be compared to another Task')

        return self.priority > other.priority

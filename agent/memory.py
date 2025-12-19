class Memory:
    def __init__(self):
        self.data = {}

    def update(self, key, value):
        self.data[key] = value

    def missing(self):
        required = ["income"]
        return [r for r in required if r not in self.data]

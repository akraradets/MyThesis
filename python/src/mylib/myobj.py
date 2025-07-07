class MyObj:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    def __repr__(self):
        return f"MyObj(name={self.name})"
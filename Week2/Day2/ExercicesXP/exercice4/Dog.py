class Dog():
    def __init__(self, name, height=50):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")
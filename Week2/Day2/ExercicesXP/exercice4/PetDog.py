from Dog import Dog
import random

class PetDog(Dog):
    def __init__(self, name, height=50):
        super().__init__(name, height)
        self.trained = False

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        names = [self.name, *args]
        print(" ".join(names) + " all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
my_dog = PetDog("Rex")

my_dog.play("Milo", "Max")

my_dog.train()

my_dog.do_a_trick()

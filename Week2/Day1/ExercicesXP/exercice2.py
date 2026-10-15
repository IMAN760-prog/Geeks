class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f"{self.name} is barking "
    def run_speed(self):
        return f"dog’s running speed is {self.weight/self.age*10}"

    def fight(self, other_dog):
        self.score = self.run_speed()*self.weight
        self.other_score = other_dog.run_speed()*other_dog.weight
        if self.score>self.other_score:
            return f"{self.name} wins the fight"
        elif self.score<self.other_score:
            return f"{other_dog.name} wins the fight"
        else:
            return f"It's a tie"
dog1 = Dog("Rix", 3, 10)
dog2 = Dog("Max", 2, 8)

print(dog1.bark())
print(dog1.run_speed())
print(dog1.fight(dog2))
        
    
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        self.groups = {}

        for animal in self.animals:
            letter = animal[0].upper()

            if letter not in self.groups:
                self.groups[letter] = []

            self.groups[letter].append(animal)

    def get_groups(self):
        self.sort_animals()

        for letter, animals in self.groups.items():
            print(f"{letter}: {animals}")


new_york_zoo = Zoo("New York Zoo")

new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Lion")
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")

print("Zoo name:", new_york_zoo.name)

print("All animals:")
new_york_zoo.get_animals()

new_york_zoo.sell_animal("Lion")

print("Animals after selling Lion:")
new_york_zoo.get_animals()

print("Animal groups:")
new_york_zoo.get_groups()



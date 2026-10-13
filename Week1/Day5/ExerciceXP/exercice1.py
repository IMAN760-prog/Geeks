class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1 = Cat("Mino",5)
cat2 = Cat("Trizore",2)
cat3 = Cat("Sindy",3)
def find_the_oldest_cat():
    return max([cat1, cat2, cat3],key=lambda Cat: Cat.age)

oldest_cat = find_the_oldest_cat()

print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old") 
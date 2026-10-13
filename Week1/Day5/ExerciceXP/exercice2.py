class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
       print(self.name," goes woof!")

    def jump(self):
        x = self.height*2
        print(f"{self.name}, jumps,{x}cm high!")
davids_dog=Dog("Rex",50)
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog=Dog("Teacup",20)
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()  
if davids_dog.height > sarahs_dog.height:
      print(davids_dog.name ,"is bigger" )
else:
      print(sarahs_dog.name ,"is bigger")



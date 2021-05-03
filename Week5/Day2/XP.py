from random import randint

# Exercise 1 : Pets
# Using this code:

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Tabby(Cat):
    def sing(self,sounds):
        return f'{sounds}'
# Add another cat breed.
# Create a list of all of the pets (create three cat instances from the above) my_cats = []
cat1=Bengal("Mookie",4)
cat2=Chartreux("Fluffy",2)
cat3=Tabby("Stripes",1)
my_cats=[cat1,cat2,cat3]
# Instantiate the Pet class with all your cats. Use the variable my_pets
my_pets=Pets(my_cats)
my_pets.walk()
# Output all of the cats walking using the my_pets instance


# Exercise 2 : Dogs
# Create a class named Dog with the attributes name, age, weight
class Dog():
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
        
# Implement the following methods for the class:
# bark: returns a string of “<dog_name> barks”.
    def bark(self):
        return (f"{self.name} barks")
# run_speed: returns the dogs running speed (weight/age*10).
    def run_speed(self):
        return self.weight/self.age*10
# fight : gets parameter of other_dog, returns string of which dog won the fight between them, whichever has a higher run_speed x weight should win.
    def fight(self,other_dog):
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            return f"{self.name} won the fight against {other_dog.name}"
        else:
            return f"{other_dog.name} won the fight against {self.name}"
# Create 3 dogs and use some of your methods
dog1=Dog("Spot",4,35)
dog2=Dog("Pip",1,20)
dog3=Dog("Rex",7,60)

print(dog1.bark())
print(dog2.run_speed())
print(dog3.fight(dog1))
# Exercise 3 : Dogs Domesticated
# Create a new python file and import your Dog class from the previous exercise.
class PetDog(Dog):
    def __init__(self,name,age,weight,trained=False):
        super().__init__(name,age,weight)
        self.trained=trained
# Create a class named PetDog that inherits from Dog.
# Add the attribute trained (boolean) to the PetDog class, should always start False
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
    def train(self):
        print(self.bark())
        self.trained=True
# play: gets parameter of any amount of other dogs (look up *args) and prints “the dogs: *dog_names play together” each of the dogs that plays has their trained boolean switched to False
    def play(self,*other_dogs):
        print("The dogs:", end=" ")
        for dog in other_dogs:
            print(f"{dog.name},",end=" ")
            dog.trained=False
        print(f"and {self.name} play together.")
# do_a_trick: will print one of the following sentences randomly ONLY IF the dogs trained boolean is True, after doing the trick the trained boolean moves to False
    def do_a_trick(self):
        tricks=["does a barrel roll","stands on her back legs","shakes your hand","plays dead"]
        rand_num=randint(0,len(tricks)-1)
        if self.trained==True:
            print(f"{self.name} {tricks[rand_num]}")
            self.trained=False

dog3=PetDog("Sparky",3,40,True)
dog4=PetDog("Chichi",6,20,False)
dog5=PetDog("Pooch",1,30,False)
dog3.do_a_trick()
dog4.train()
dog4.do_a_trick()
dog5.play(dog4,dog3)

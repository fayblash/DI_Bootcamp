# # Exercise 1: Cats
# # Instructions
# # Using this class

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def oldest_cat(cat_list):
#     oldest_current=cat_list[0]
#     for cat in cat_list:
#         if cat.age>oldest_current.age:
#             oldest_current=cat
#     return oldest_current
# # Instantiate three Cat objects using the code provided above.
# c1=Cat("Roxy",3)
# c2=Cat("Meow",2)
# c3=Cat("Fluffy",4)
# # Outside of the class, create a function that finds the oldest cat and returns the cat.
# all_cats=[c1,c2,c3]

# oldest=oldest_cat(all_cats)
# print(f"{oldest.name} is the oldest cat and she is {oldest.age} years old.")


    
# # Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.


# # Exercise 2 : Dogs
# # Instructions
# # Create a class called Dog.
# class Dog:
#     def __init__(self,name,height):
#         self.name=name
#         self.height=height
        
#     def bark(self):
#         print(f"{self.name} goes woof!")
# # In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# # Create a method called bark that prints the following string “<dog_name> goes woof!”.
# # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
#     def jump(self):
#         print(f"{self.name} jumps {self.height*2} cm")        
# # Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# davids_dog=Dog("Rex",50)
# print(davids_dog.name)
# print(davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()
# # Print the details of his dog (ie. name and height) and call the methods bark and jump.
# # Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# sarahs_dog=Dog("Teacup",20)
# print(sarahs_dog.name)
# print(sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()
# # Print the details of her dog (ie. name and height) and call the methods bark and jump.
# # Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
# if sarahs_dog.height>davids_dog.height:
#     print(f"{sarahs_dog.name} is bigger.")
# else:
#     print(f"{davids_dog.name} is bigger.")

# # Exercise 3 : Who’s The Song Producer?
# # Instructions
# # Define a class called Song, it will show the lyrics of a song.
# class Song:
#     def __init__(self,lyrics):
#         self.lyrics=lyrics
# # Its __init__() method should have two arguments: self and lyrics (a list).
# # Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
#     def sing_me_a_song(self):
#         for lyric in self.lyrics:
#             print(lyric)
        
# # Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# # Then, call the sing_me_a_song method. The output should be:
# stairway.sing_me_a_song()
# # There’s a lady who's sure
# # all that glitters is gold
# # and she’s buying a stairway to heaven


# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]
        self.list_animals=[]
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
# Create a method called get_animals that prints all the animals of the zoo.
    def get_animals(self):
        print(self.animals)
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example
    def sort_animals(self):
        self.animals=sorted(self.animals)
        # list_animals=[]
        temp_list=[self.animals[0]]
        for i in range(1,len(self.animals)):
            if self.animals[i][0] == temp_list[-1][0]:
                temp_list.append(self.animals[i]) 
            else:
                self.list_animals.append(temp_list)
                temp_list=[]
                temp_list.append(self.animals[i])   
            i+=1
        # print(list_animals)
        return {v+1: k for v, k in enumerate(self.list_animals)}
    
    def get_groups(self):
        for i in self.list_animals:
            print(i)

fays_zoo=Zoo("fay")
fays_zoo.add_animal("Bear")
fays_zoo.add_animal("Ape")
fays_zoo.add_animal("Cat")
fays_zoo.add_animal("Emu")
fays_zoo.add_animal("Cougar")
fays_zoo.add_animal("Eel")
fays_zoo.add_animal("Baboon")
fays_zoo.get_animals()
print(fays_zoo.sort_animals())
fays_zoo.get_groups()
# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
# 4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.
#     
        
# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe




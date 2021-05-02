# Instructions : Old MacDonald’s Farm
# Look carefully at this code and output
# File: market.py

# Create the code that is needed to recreate the code above. Here are a few questions to help give you some direction:
# 1. Create a Farm class. How do we implement that?
class Farm:
    def __init__(self,name):
        self.name=name
        self.animal_count={}
# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3. How many methods does the Farm class need ?
    def add_animal(self,animal,quantity=1):
        self.animal=animal
        self.quantity=quantity
        if animal not in self.animal_count:
            self.animal_count[animal]=quantity
        else:
            self.animal_count[animal]+=quantity
    
    def get_info(self):
        print(f"{self.name}'s farm\n")
        for k,v in self.animal_count.items():    
            print (f"{k} : {v}")
        print(f"\nE.I.E.I.O!")
    
    def get_animal_types(self):
        return sorted([k for k in self.animal_count.keys()])
    
    def get_short_info(self):
        string="s, ".join(self.get_animal_types())
        print(f"{self.name}'s farm has {string}.")
        
    # def get_animal_types(self):
    #     self.animal_list=sorted([k for k in self.animal_count.keys()])
    #     return self.animal_list
    
    # def get_short_info(self):
    #     string="s, ".join(self.animal_list)
    #     print(f"{self.name}'s farm has {string}.")
    
# 4. Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# 5. Test that your code works and gives the same results as the example above.
# 6. Bonus: line up the text nicely in columns like in the example using string formatting
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
print(macdonald.get_animal_types())
macdonald.get_short_info()
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Expand The Farm
# Add a method to the Farm class called get_animal_types. It should return a sorted list of all the animal types (names) that the farm has in it. For the example above, the list should be: ['cow', 'goat', 'sheep']


# Add another method to the Farm class called get_short_info. It should return a string like this: “McDonald’s farm has cows, goats and sheep.”
    

# It should call the get_animal_types function.
# How would we make sure each of the animal names printed has a comma after it aside from the one before last (has an and after) and the last(has a period after)?.
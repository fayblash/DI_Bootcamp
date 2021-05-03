# Exercise 1 : Family
# Create a class called Family and implement the following attributes:
class Family():
    def __init__(self,lname):
        self.lname=lname
        self.members=[{'name':'Michael','age':35,'gender':'Male','is_child':False},
                      {'name':'Sarah','age':32,'gender':'Female','is_child':False}]
                    
# members: list of dictionaries with the following keys name, age, gender and is_child (boolean).
# last_name (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:
    def born(self,**member):
        self.members.append(member)
        print(f"\nCongratulations {self.lname} family on the birth of baby {member['name']}!")
# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
        def is_18(self,name):
            for member in self.members:
                if member['name']==name and member['age'] >=18:
                    return True
                else:
                    return False
                
# a method that prints all the members of the family.
    def print_fam(self):
        print(f"The members of the {self.lname} family are: ",end="")
        for member in self.members:
            print (f"{member.get('name')}", end=" ")
        print("\n")
family1=Family("Blashka")
family1.print_fam()
nava={"name":"Nava","age":0,"gender":"Female","is_child":True}
family1.born(**nava)
family1.print_fam()


# Exercise 2 : TheIncredibles Family
# Create a class called TheIncredibles. this class should inherit from the Family class:
class TheIncredibles(Family):
    def __init__(self,lname):
        super().__init__(lname)
        self.members=[{'name':'Bob','age':35,'gender':'Male','is_child':False,'power':'superhuman strength','incredible_name':'Mr.Incredible'},
        {'name':'Helen','age':35,'gender':'Female','is_child':False,'power':'stretch and reshape her body','incredible_name':'Elastigirl'},
        {'name':'Violet','age':14,'gender':'Female','is_child':True,'power':'invisibility','incredible_name':'Violet'},
        {'name':'Dashiel','age':11,'gender':'Male','is_child':True,'power':'superspeed','incredible_name':'Dash'},
        ]
# This is no random family they are an incredible family therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Add a method called use_power,this method should print the power of a member if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
    def use_power(self):
        for member in self.members:
            if member['age'] > 18:
                print(f"{member['name']}'s superpower is {member['power']}")
# add a method called incredible_presentation which presents the family members with their incredible names and powers.
    def incredible_presentation(self):
        print(f"Introducing the {self.lname}'s!")
        for member in self.members:
            print(f"{member['incredible_name']} whose superpower is {member['power']}")
            
# Look up the names of The Incredibles characters on google and build the family (if you can’t find the correct information just improvise).
the_incredibles=TheIncredibles("Parr")
# Print their normal presentation and their incredible presentation.
the_incredibles.print_fam()
the_incredibles.incredible_presentation()
# Use the born method inherited from the family class to add Baby Jack with the following power: “Unknown Power”.
jack={'name':'Jack','age':0,'gender':'Male','is_child':True,'power':'unknown','incredible_name':'JackJack'}
the_incredibles.born(**jack)
# Print both presentations again. Check that Baby Jack is born and that his power is showing when using the incredible representation.
the_incredibles.incredible_presentation()
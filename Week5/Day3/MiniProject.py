# Mini-Project: Characters Game
# Description
# Create a class called Character with the following attributes and methods:
# name
# life – starts with a default value of 20
# attack – the base attack of a character (integer) will be a default of 10
# basic_attack() - accepts another character as a parameter and will <attack> the character and the characters <life> points should drop.
class Character():
    all_characters=[]
    
    def __init__(self,name,life=20,attack=10):
        self.name=name
        self.life=life
        self.attack=attack
        self.all_characters.append(self)
    
    def basic_attack(self,other):        
        other.life-=1
    
    def show_lifeattack(self):
        print(f"{self.name} has {self.life} lives left and {self.attack} attacks left.")    


# Instructions
# Now create 3 different classes that inherit from Character:
# Every character type should say (ie. print) something when they are created, get creative :)
# Druid:
# meditate() - increase life by 10, decrease attack by 2
# animal_help()- increase attack by 5
# fight() - accepts another character as a parameter and subtracts (0.75*life + 0.75*attack) from the other characters life.
# Example:
# druid.fight(other_char): other_char.life - (0.75*self.life + 0.75*self.attack)
class Druid(Character):
    def __init__(self,name,life=20,attack=10):
        super().__init__(name,life=20,attack=10)
        print(f"I am a Druid named {name} and I love to meditate")
    
    def meditate(self):
        self.life+=10
        self.attack-=2
    
    def animal_help(self):
        self.attack+=5
    
    def fight(self,other_char):
        other_char.life -= (0.75*self.life + 0.75*self.attack)
# Warrior:
# brawl() - accepts another character as a parameter, subtacts (2*attack) to the other characters life and adds (0.5*attack) to his own life.
# train() - increase both your attack and life points by 2.
# roar() - accepts another character as a parameter and subtracts their attack points by 3.
class Warrior(Character):
    def __init__(self,name,life=20,attack=10):
        super().__init__(name,life=20,attack=10)
        print(f"I am a Warrior named {name} and I love to fight")
    
    def brawl(self,other_char):
        other_char.life-=2*self.attack
        self.life+=0.5*self.attack
    def train(self):
        self.attack+=2
        self.life+=2
    def roar(self,other_char):
        other_char.attack-=3
# Mage:
# curse() – accepts another character as a parameter and subtracts their attack points by 2.
# summon() - increases attack attribute by 3 points.
# cast_spell() - accepts another character as a parameter and subtracts attack/life to the other characters life points (eg if your attack is 20 and life is 5 you will subtract 4 life points).
class Mage(Character):
    def __init__(self,name,life=20,attack=10):
        super().__init__(name,life=20,attack=10)
        print(f"I am a Mage named {name} and I love to do magic")
    
    def curse(self,other_char):
        other_char.attack-=2
    
    def summon(self):
        self.attack+=3
    
    def cast_spell(self,other_char):
        other_char.life-=self.attack/self.life 
   
# Once all your classes are created start testing them, create one of each character and use each of their methods.
druid1=Druid("Druid Dude")
warrior1=Warrior("War Guy")
mage1=Mage("Magic Mage")

druid1.meditate()
warrior1.train()
mage1.summon()

for char in Character.all_characters:
    char.show_lifeattack()

warrior1.roar(mage1)
mage1.cast_spell(warrior1)
druid1.fight(mage1)

for char in Character.all_characters:
    char.show_lifeattack()
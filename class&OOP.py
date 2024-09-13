class Monster1:
    def __init__(self, func):
        self.func = func

class Attacks:
    def bite(self):
        print("Bite")
    def strike(self):
        print("strike")
    def slash(self):
        print("slash")
    def kick(self):
        print("kick")

monster1 = Monster1(Attacks().bite) 
# Here we use "Attacks()" because the 'self' in each sub-functions
# We need Attacks as an object instead of class
monster1.func()
# Without the parenthesis, the func will not be triggered

# SCOPE
class Hero:
    def __init__(self, damage, monster):
        self.damage=damage
        self.monster=monster

    def attack(self):
        self.monster.get_damage(self.damage)

class Monster2:
    def __init__(self, health, energy):
        self.health=health
        self.energy=energy

    def get_damage(self, amount):
        self.health -= amount

monster2 = Monster2(health=100, energy=50)
hero1 = Hero(damage=15,monster=monster2)
hero1.attack()
print(monster2.health)

# INHERITANCE
class Monster3:
    def __init__(self, health, energy):
        self.health=health
        self.energy=energy

    def attack(self,amount):
        print('The monster has attacked!')
        print(f'{amount} damage has dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')
  
# Child class
class Shark1(Monster3):
    def __init__(self, speed, health, energy):
        # Monster3.__init__(self, health, energy)
        super().__init__(health, energy) # same effect as the line above
        self.speed = speed
    
    def bite(self):
        print('The shark has bitten')
    
    def move(self):
        print('The shark has moved')
        print(f'The speed of the shark is {self.speed}')

class Scorpion(Monster3):
    def __init__(self, scorpion_health, scorpion_energy, p_damage):
        super().__init__(scorpion_health, scorpion_energy)
        self.p_damage = p_damage

    def attack(self, p_damage):
        print('The scorpion emitted poison')
        print(f'{p_damage} has dealt')

shark = Shark1(health=150, energy= 40, speed = 120)
shark.move()

# Complex Inheritance
class Monster4:
    def __init__(self, health, energy, **kwargs):
        print(kwargs)
        self.health=health
        self.energy=energy
        super().__init__(**kwargs)

    def attack(self,amount):
        print('The monster has attacked!')
        print(f'{amount} damage has dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        print(kwargs)
        self.speed=speed
        self.has_scales=has_scales
        super().__init__(**kwargs)
    
    def swim(self):
        print(f'The fish is swimming at a speed of {self.speed}')

class Shark2(Monster4, Fish):
    def __init__(self, health, energy, speed, has_scales, bite_strength):
        self.bite_strength=bite_strength
        super().__init__(health=health, energy=energy, speed=speed, has_scales=has_scales)

# mro -> method resolution order
# shows in what order python would go through the classes
# Since Monster3 is handled before Shark2, so no kwargs in Shark2
print(Shark2.mro())

shark = Shark2(
    bite_strength=50, 
    health=200, 
    energy=55, 
    speed=120, 
    has_scales=False
)

print(shark.speed)

# Classes extra parts
class Monster5:
    '''A monster that has some attributes'''
    def __init__(self, health, energy):
        self.health=health
        self.energy=energy

        # Private Attributes
        self._id=5 
        #By convention, variable with an underscore 
        #in front of them are not supposed to be changed

    def attack(self,amount):
        print('The monster has attacked!')
        print(f'{amount} damage has dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

monster3=Monster5(20,10)

# hasattr and setattr
print(hasattr(monster3,'health')) # Check if monster3 has the attribute health
setattr(monster3, 'health', 2000) # Set the health of monster3 to 2000

new_attributes={'health':2000, 'attack':1000, 'mana':500}
for attr, value in new_attributes.items():
    setattr(monster3, attr, value)
    # It will generate a new attribute and avoid AttributeNotFound Error

# doc
print(monster3.__doc__) # demonstrate the annotation of a class


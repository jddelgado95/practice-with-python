## Here we are explaining inheritance, which is the capacity of create subclass that are capable of inherit the capabilities of its parent classes. This is useful to avoid repeated proccesses, or repeated code. 

## Polymorphism is another pillar of OOP. Classes and objects can share methods, but they not necessarily works the same way from one class to another. 

class User(object): 
    #def __init__(self, email):
    #    self.email = email
    def sign_in(self):
        print('logged in')
    #def attack(self):
    #    print('Do nothing') ## this method will be overwrite by the other attack methods from child classes. That's polymorphism. 

class Wizard(User): ## pass the parent class
    def __init__(self, name, power):
        #User.__init__(self, email) ## we can do this, but there's a better method. User super
        #super().__init__(self, email) ## referes to the super class, the class above Wizard, which is User. The super() function is used to give access to methods and properties of a parent or sibling class. The super() function returns an object that represents the parent class
        self.name = name 
        self.power = power
    
    def attack(self):
        #User.attack(self) ## allows me to use the parent class method attack() within my child class
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name 
        self.num_arrows = num_arrows
    def remain_arrows(self):
        print(f'attacking with power of {self.num_arrows} arrows')
    
    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


## built-in Python function that checks if an object is an instance of a specified class or a tuple of classes. It returns True if the object matches the type, and False otherwise. It is commonly used for type checking, offering flexibility by supporting inheritance and multiple types

wizard1 = Wizard('Merlin',50)
archer1 = Archer('Robin',100)
hb1 = HybridBorg('Wall-E',100,1) ##inherits both archer and wizard
##print(isinstance(wizard1, Wizard)) ## should print TRUE
##print(isinstance(wizard1, User)) ## should print TRUE
## In Python, the object class serves as the root of the class hierarchy. Every class, by default, directly or indirectly inherits from object. This inheritance ensures that all classes possess fundamental attributes and methods defined by the object class.
## When a class is defined without explicitly specifying a base class, Python automatically makes it a subclass of object
##print(isinstance(wizard1, object)) ##should print TRUE
#wizard1.attack()
#archer1.attack()
#def player_attack(char):
    #char.attack()
#player_attack(wizard1) ## both functions works the same but results are not the same. 
#player_attack(archer1)
#print(wizard1.email) ## prints an error because even if we might inherit, we can not inherit a constructor this easy. We can add an email attribute to the init in the wizard class, but that's not efficient. 
## we =want to call the init function from user within the wizard class


#instrospection: is the ability to know the type of an object at runtime. 
#print(dir(wizard1)) ## gives all the methods and attributes of Wizard() class.

print(hb1.run())
print(hb1.remain_arrows())
print(hb1.attack())

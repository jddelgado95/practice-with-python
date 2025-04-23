## Python advanced OOP 
## Everything in Python is an object
## An object has attributes and methods
## We can create our own data types using classes and objects, with their own attributes and methods
## is a paradigm, it enforces us to think about our code, its purpose, and makes us structure it. 

# convention: camelcase for classes
#class BigObject: ## this class is only a blueprint
    # code
#    pass
#obj1 = BigObject() #this is the actual object, which is an instance of the class. 
#print(type(obj1))

## Let's say we work for video game company:
class PlayerCharacter:
    membership = True ## Class object attribute. Is not dynamic, it is static
    ## special method, dunder method or magic method. WE use it as a constructor method or init methd. 
    ## it is called automatically everytime we call an object or a class
    ## self defines the class where its being called
    def __init__(self, name, age): 
        if (PlayerCharacter.membership):
            self.name = name ## atributes
            self.age = age

    def run(self):
        print('run')
        return 'done' ## to avoid the none printed if we dont use a return 
    
    def shout(self):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Juan',33)
player2 = PlayerCharacter('Pedro',44)
print(player1)    
print(player1.name) 
print(player1.age) 
print(player2)    
print(player2.name) 
print(player2.age) 
print(player1.run())
#help(player1) ## prints the entire blueprint of the object
print(player1.membership)
print(player1.shout())
print(player2.shout())

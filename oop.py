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
    def __init__(self, name='anonymous', age=20): 
        if (age > 18):
            self.name = name ## atributes
            self.age = age

    def run(self):
        print('run')
        return 'done' ## to avoid the none printed if we dont use a return 
    
    def shout(self):
        print(f'my name is {self.name}')
    
    ## is an inbuilt function in Python, which returns a class method for a given function. This means that classmethod() is a built-in Python function that transforms a regular method into a class method. When a method is defined using the @classmethod decorator (which internally calls classmethod()), the method is bound to the class and not to an instance of the class. As a result, the method receives the class (cls) as its first argument, rather than an instance (self)
    @classmethod 
    def adding_things(cls,num1, num2):
        return cls('Teddy',num1 + num2) # here i can instantiate an object Teddy, with age num1 plus num2

    ## is a decorator used to define a static method within a class. Static methods are functions that are bound to the class and not the instance of the class. They do not receive an implicit first argument (neither self nor cls) and cannot access or modify the class state
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Juan',33)
print(player1.adding_things(2,3))
print(PlayerCharacter.adding_things(2,3)) ## we don't need the object, we can use the class
player2 = PlayerCharacter('Pedro',44)
player3 = PlayerCharacter() # here we are using the default parametersof the constructor
player4 = PlayerCharacter.adding_things(2,3)
print(player4)
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
print(player3)
print(player3.shout())

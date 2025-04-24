## 4 pillars of OOP
## Encapsulation is the binding of data (attributes) and functions (methods) within classes. 
## Abstraction: hidding / abstracting information and getting exterior users the necessary access to what we want, so data can be protected or sensible code can be protected. 
class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
    
    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')

player1 = PlayerCharacter('andrei',100)
print(player1.speak()) ## this allows me to access the method speak
player1.name = '!!!!'
player1.speak = 'BOOOO'
#print(player1.speak()) #TypeError: 'str' object is not callable
print(player1.speak) ## now I can modify the methods outcome, which is not good because everyone can have access to this and modify it. 
## Dunder Methods: 
## Python Magic methods are the methods starting and ending with double underscores ‘__’. They are defined by built-in classes in Python and commonly used for operator overloading. They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.

class Toy(): 
    def __init__(self, color, age): 
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False 
        }

    ## lets modify the str method and make it our own
    def __str__(self):
        return f'{self.color}'
    
    # we can change the meaning of len method
    def __len__(self):
        return 5
    
    #def __del__(self):
    #    print('deleted!')

    def __call__(self):
        return('yes?')
    
    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure)) ## both lines, this and the above one, do the same. 
print(len(action_figure))
#del action_figure
print(action_figure())
print(action_figure['name'])
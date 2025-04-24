class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name 
        self.age = age

# 1 Instantiate the Cat object with 3 cats 
orange_cat = Cat('Rogelio',4)
tux_cat = Cat('Tento',2)
gray_cat = Cat('Rich',7)
# 2 Create a function that finds the oldest cat
def find_oldest(*args):
    return max(args) #returns the item with the highest value, or the item with the highest value in an iterable

# 3 Print out: "The oldest cat is x years old." x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {find_oldest(orange_cat.age, tux_cat.age,gray_cat.age)} years old')
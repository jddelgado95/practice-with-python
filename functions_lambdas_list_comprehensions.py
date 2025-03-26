## Showing the implemetation of a simple function
def example_function(x):
    return x+1

example_variable = 10
print(example_function)

processed_variable = example_function(example_variable)
print(processed_variable)

def complicated_function(x,y):
    def squared(z):
        return z*z

    x_squared = squared(x)
    return x_squared + y * 3

x = 5
y = 3

print(complicated_function(x,y))

## Show how to use list comprehension
## Normal problem
xs = [0,1,2,3,4,5]

result = []
for x in xs:
    result.append(x*x)

print(result)

## Enhance version with list comprehension
result_alternative = [(x*x) for x in xs]
print(result_alternative)


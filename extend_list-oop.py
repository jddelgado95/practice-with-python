## Here we are going to extend the list method

## we only have add the parent class list to SuperList, so it can inherit all the methods from built-in list class in Python
class SuperList(list): 
    def __len__(self):
        return 1000
    

super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList,list)) #prints True
    
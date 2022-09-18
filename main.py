nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

nested_list_2 = [
	['a', ['b_1', 'b_2', 'b_3'], 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

test_list = ['a', 1, 5]

# task 1 - Integrator

class FlatIterator():
    def __init__(self, user_list):
        self.list = user_list
    
    def __iter__(self):
        self.coursor= 0
        self.coursor_form = -1
        return self
     
    def __next__(self):
       
        if self.coursor_form < len(self.list[self.coursor])-1:
            self.coursor_form +=1
        else:
            self.coursor_form=0
            self.coursor += 1
                
        if self.coursor == len(self.list):
            raise StopIteration
                
        
        
        return self.list[self.coursor][self.coursor_form]
    
   
    

my_list = FlatIterator(nested_list)
for item in my_list:
    print(item)




# task 2 - Generator

def flat_generator(user_list):
    for i in user_list:
        if isinstance(i, list):
            yield from flat_generator(i)
        else:
            yield i
            
my_list = flat_generator(nested_list)
for i in my_list:
    print(i)






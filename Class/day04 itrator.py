#iterator--> repeations

""" max_num=int(input("Enter a number : "))

class Square_iterator:
    def __init__(self, max_num):
        self.max_num=max_num
        self.counter=0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter<=self.max_num:
            self.counter+=1
            squared=self.counter*self.counter
            return squared
        else:
            raise StopIteration

squared=Square_iterator(max_num)

for i in squared:
    print(i)
 """
#generator ---> for code optimaization

n=int(input("Enter a number: "))
def even_nums(n):
    for i in range(0,n,2):
        yield i

for i in even_nums(n):
    print(i)
    
    



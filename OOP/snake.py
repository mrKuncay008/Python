class Snake: # class Snake

    def __init__(self):
        self.victims = 1

    def increment(self):
        self.victims += 1

class Mouse:
    def __init__(self):
        if Snake != Mouse:
            self.victims - 1

if __name__ == '__main__':
    print("Hallo ini ", Mouse,"and",Snake)
else:
    print("Hallo ini ", Mouse.__name__,"and",Snake.__name__)
    
print(Snake.__module__)
print(Snake.__name__," ", Mouse.__name__)
print(Snake.__subclasses__, "\n", Mouse.__dict__)

print(Snake, "Makan", Mouse)

# def f(x):
#     try:
#         x = x / x
#     except:
#         print("a",end='')
#     else:
#         print("b",end='')
#     finally:
#         print("c",end='')
 
 
# f(1)
# f(0)

# class I:
#     def __init__(self):
#         self.s = 'abc'
#         self.i = 0
 
#     def __iter__(self):
#         return self
 
#     def __next__(self):
#         if self.i == len(self.s):
#             raise StopIteration
#         v = self.s[self.i]
#         self.i += 1
#         return v
 
 
# for x in I():
#     print(x,end='')


#
# class House:
#     name = True
#     houses_history = []
#     def __new__(cls, *args, **kwargs):
#         if name not in cls.houses_history :
#
#             return object().__new__(cls)
#
#
#     def __init__(self, houses_history, name, number_of_floors):
#         self.args = args
#         self.kwargs = kwargs
#         for key, value in kwargs.items():
#             setattr(self,key,value)
#     #def __del__(self):
#
#
#
# houses_history =[1]
# house = {'name': 'ЖК Эльбрус', 'number_of_floors' : 10}
# h1 = House(*houses_history, **house)




class House:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object().__new__(cls)

    def __init__(self,*args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self,key,value)

    def __del__(self, name):
        print(f'{self.name}  снесён, но он останется в истории')

houses_history =[1]
house = {'name': 'ЖК Эльбрус', 'number_of_floors' : 10}
h1 = House(*houses_history, **house)
print(houses_history)
print(h1.name)
print(h1.number_of_floors)
print(h1.args)
print(h1.name, h1.number_of_floors)
#del h1.name
# class House:
#
#     houses_history = []
#
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#
#     def __init__(self, first, second, third):
#         print(first)
#         print(second)
#         print(third)
#
#     def __del__(self, name):
#          print(f'{self.name}  снесён, но он останется в истории")
#
#
#
# h1= House('date', second= 25, third = 3.14)
# h2 = House('date', second=30, third = 40)
# del h1
# print(h2)

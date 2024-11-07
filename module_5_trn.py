
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self,new_floor):
        #nf = [i for i in range(1, new_floor+1)] # генератор списка для создания произвольного списка целых чисел
        nf = list(range(1, new_floor+1))
        if new_floor > self.number_of_floors:
           print("Такого этажа не существует")
        else:
            print(*nf[:], sep="\n")

    def __len__(self):
        return  self.number_of_floors

    def __str__(self):
       return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


    # def __add__(self, other):
    #     if isinstance(other, int):  # and isinstance(other, House):#and isinstance(Houses, int)
    #         return self.number_of_floors + other
    #     # return  self.number_of_floors + other.number_of_floors
    #
    #
    # def __radd__(self, other):
    #     return self.number_of_floors
    #
    #
    # def __iadd__(self, other):

    #     return self.number_of_floors

    def __add__(self, other):
        if isinstance(other, House):
            return self.number_of_floors + other.number_of_floors #House(self.number_of_floors + other.number_of_floors)

        else:
            return self.number_of_floors + other #House(self.number_of_floors + other)

    def __radd__(self, other):
        return self.__add__(other)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1+10)
print(h1)

print((h1+10).number_of_floors)
print(h1)


# class Human:
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#         self.say_info()
#         self.birthday()
#
#     def say_info(self):
#         print(f'Меня зовут {self.name}, мне {self.age}')
# # без f {self.name} и {self.age} не переводятся в знаьения:"Меня зовут {self.name}, мне {self.age}"
#
#     def birthday(self):
#         self.age += 1
#         print(f'У меня день рождения, мне {self.age}')
#         if self.age >= 25:
#             print('Вы можете получить водительские права')
#
#
# max = Human('Максим', 22)
# print(max.name,max.age) #здесь будет не 22, а 23 года, поскольку мы изменили год, применив self.birthday() перед этим
# print(max.age)
# #max.birthday()
# #max.birthday()
#

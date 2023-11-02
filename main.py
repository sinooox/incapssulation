class Human:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def output(self):
        print(f'name - {self.__name}')
        print(f'age - {self.__age}')
        print(f'height - {self.__height}')
        print('-'*30)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if len(name) > 2 and len(name) < 20:
            self.__name = name
        else:
            print('error')
            
    @property
    def age(self):
        return self__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            print('error')

p1 = Human('Мухаммэд', 21, 168)
p1.output()

p1.name = 'Дэнис'
p1.age = 78
p1.output()

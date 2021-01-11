class Dog:
    # things which happen when class if first created
    
    def __init__(self,name,age):
        # self refers to the instance
        self.name = name
        self.age = age
    
    def speak(self):
        print("Hi i am", self.name, "my age is", self.age)

    def change_age(self,age):
        self.age = age

    def add_weight(self,weight):
        self.weight = weight


dog = Dog('neil',7)
dog.speak()
dog.change_age(4)
dog.speak()

dog.add_weight(85)

print(dog.age) # public access
print(dog.weight)


# inheritance

class Dog_new:
    def __init__(self,name,age):
        # self refers to the instance
        self.name = name
        self.age = age
    
    def speak(self):
        print("Hi i am", self.name, "my age is", self.age)

    def talk(self):
        print('bark!')

class Cat(Dog_new):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def talk(self):
        print('Meow!')

tim = Cat('tim',5,'blue')
tim.speak()
tim.talk()


class Vechicle:
    def __init__(self,price,gas,color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Car(Vechicle):
    def __init__(self,price,gas,color,speed):
        super().__init__(price,gas,color)
        self.speed = speed

    def beep(self):
        print('Beep beep')

class Truck(Vechicle):
    def __init__(self,price,gas,color,tires):
        super().__init__(price,gas,color)
        self.tires = tires

    def beep(self):
        print('Honk honk')

car = Car(25,25,'orange',45)
car.beep()


class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self,x,y):
        self.x += x
        self.y += y

    def __add__(self,p):
        return Point(self.x+p.x, self.y + p.y)

    def __sub__(self,p):
        return Point(self.x-p.x, self.y - p.y)

    def __mul__(self,p):
        return self.x*p.x + self.y*p.y

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self,p):
        return self.length() > p.length()

    def __ge__(self,p):
        return self.length() >= p.length()

    def __lt__(self,p):
        return self.length() < p.length()

    def __le__(self,p):
        return self.length() <= p.length()

    def __eq__(self,p):
        return self.x == p.x and self.y == p.y

    def __str__(self,p):
        return "(" + str(self.x) + ',' + str(self.y) + ")"

    

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

print(p1 == p2)
print(p1 > p2)
print(p4 <= p3)


class Dog_new_:
    dogs = [] # class variable
    
    def __init__(self,name):
        self.name = name
        self.dogs.append(self)

    @classmethod # decorators
    def num_dogs(cls): # can be called on name of class
        return len(cls.dogs)

    @staticmethod # dont't need class to be passed
    # inside static method we cannot access the class methods, because self
    # is not available
    def bark(n): # only pass params we want
        """barks n times"""
        for _ in range(n): 
            print("bark")

tim = Dog_new_("Tim")
jim = Dog_new_("Jim")

# acess class variables

print(Dog_new_.dogs)
print(Dog_new_.num_dogs())

Dog_new_.bark(5)

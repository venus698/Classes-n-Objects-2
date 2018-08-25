#Question 1
class circle:
    def __init__(self):
        self.radius=20
    def getArea(self):
        self.area=3.14*(self.radius**2)
        print(self.area)
    def getcircumference(self):
        print(2*3.14*self.radius)
a=circle()
a.getArea()
a.getcircumference()

#Question 2

class student:
    def __init__(self):
        self.name=input("Enter Name:")
        self.rollno=int(input("Enter Rollno:"))
        self.age=0
        self.marks=0
    def display(self):
        print("Student Info-")
        print(self.name,self.rollno,self.age,self.marks)
    def setAge(self):
        self.age=int(input("Enter Age:"))
    def setmarks(self):
        self.marks=int(input("Enter Marks:"))
a=student()
a.setAge()
a.setmarks()
a.display()


#Question 3

class temperature:
    def __init__(self):
        self.ctemp=0
        self.ftemp=0
    def convertFahrenheit(self):
        self.ctemp=float(input("Enter temperature in celsius:"))
        self.ftemp=self.ctemp*1.8+32
        print(self.ctemp,"Celsius=",self.ftemp,"Fahrenheit")
    def convertcelsius(self):
        self.ftemp=float(input("Enter temperature in fahrenheit:"))
        self.ctemp=(self.ftemp - 32) * 0.5556
        print(self.ftemp,"Fahrenheit=",self.ctemp,"Celsius")
a=temperature()
a.convertFahrenheit()
a.convertcelsius()

#Question 4

class MovieDetails:
    def Display(self):
        print("Movie Details:")
        print("Artist Name:",self.artistname,"\nYear Of Release:-",self.year,"\nRating:",self.rating)
    def Add(self):
        self.artistname=input("Enter Artist Name: ")
        self.year=int(input("Enter year Of release: "))
        self.rating=float(input("Enter The Rating:"))
a=MovieDetails()
a.Add()
a.Display()

#Question 5

class animal:
    def info_(self):
        print("Animal Class")
class animal_attribute():
    def attribute(self):
        print("Animal_Attributes")
class tiger(animal,animal_attribute):
    def s(self):
        print("Tiger Class")
a=animal()
b=animal_attribute()
c=tiger()
c.info_()
c.attribute()

#Question 6

ANS- geting error because interprator wants '(' this  in line no 14&15  AFTER  solving error output is
'A', 'B'
'A', 'B'


#Question 7

class shape:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
        
class square(shape):
    def __init__(self, shape):
        self.length= shape.length
        self.breath= shape.breath
        self.area
    def area(self):
        area = self.length * self.breath
        print("Area of the square= ", area)


class rectangle(shape):
    def __init__(self, shape):
        self.length= shape.length
        self.breath= shape.breath
        self.area
    def area(self):
        area = self.length * self.breath
        print("Area of the rectangle= ", area)

length = int(input("Enter length:'"))
breadth = int(input("Enter breadth:"))
s = shape(length,breadth)
sq = square(s)
re = rectangle(s)
if length==breadth:
    sq.area()
else:
    re.area()


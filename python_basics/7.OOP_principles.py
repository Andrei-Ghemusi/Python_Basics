from abc import abstractmethod, ABC

'''1.
ABSTRACTION
Abstract class GeometricForm
Contains a field PI=3.14
Contains an abstract method area
Contains a method describe() - prints ‘Most likely I have corners’
'''
class GeometricForm(ABC):
    PI = 3.14

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print('Most likely I have corners.')

'''
2.INHERITANCE
Class Square - inherits GeometricForm
constructor for side
'''
class Square(GeometricForm):

    def __init__(self, side):
        self.__side = side

    @property
    def square_side(self):
        pass

    @square_side.getter
    def square_side(self):
        return self.__side

    @square_side.setter
    def square_side(self, side):
        self.__side = side

    @square_side.deleter
    def square_side(self):
        self.__side = None

    def area(self):
        area = self.__side ** 2
        return area

    def corners(self, nr_corners):
        if nr_corners <= 0:
            print('I do not have corners.')
        else:
            self.describe()


object = Square(2)
print(f'The area of the square is: {object.area()}')
print(f'The object before update, through getter: {object.square_side}')
object.square_side = 5
print(f'The object after update, through getter: {object.square_side}')
del object.square_side
print(f'The object returned after deleter: {object.square_side}')


'''
3.ENCAPSULATION
side is private property
Implement getter, setter, deleter for side
Implement the required interface method
Class Circle - inherits GeometricForm
constructor for radius
radius is private property
Implement getter, setter, deleter for radius
Implement the required interface method - use the PI field inherited from the parent class in the calculation
'''
class Circle(GeometricForm):

    def __init__(self,radius):
        self.__radius = radius

    @property
    def circle_radius(self):
        pass

    @circle_radius.getter
    def circle_radius(self):
        return self.__radius

    @circle_radius.setter
    def circle_radius(self, radius):
        self.__radius = radius

    @circle_radius.deleter
    def circle_radius(self):
        self.__radius = None

    def area(self):
        print(f'The area of the circle is {self.__radius * self.PI}')

    def corners(self, nr_corners):
        if nr_corners == 0:
            print('I do not have corners')
        else:
            self.describe()

object2 = Circle(9)
object2.area()
print(f'Object 2 before update, through getter {object2.circle_radius}')
object2.circle_radius = 4
print(f'Object 2 after update, through getter {object2.circle_radius}')
del object2.circle_radius
print(f'Object 2 after deleter {object2.circle_radius}')


object_corners_square = Square(4)
object_corners_square.corners(4)

object_corners_circle = Circle(7)
object_corners_circle.corners(0)



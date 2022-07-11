#!/usr/bin/python3
"""
rectangle that inhertis from Base class
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method
        """
        self.width = self.hw_validator("width", width)
        self.height = self.hw_validator("height", height)
        self.x = self.xy_validator("x", x)
        self.y = self.xy_validator("y", y)
        super().__init__(id)

    def to_dictionary(self):
        """
        Returns a dictionary rep of a rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def __str__(self):
        """custom __str__ method for rectangle
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        updates attributes
        """
        attrs, i = ['id', 'width', 'height', 'x', 'y'], 0
        if args:
            for value in args:
                setattr(self, attrs[i], value)
                i += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def display(self):
        """displays using #
        """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def area(self):
        """
        Returns: area of object
        """
        return self.__width * self.__height

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        """
        self.__width = self.hw_validator("width", value)

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        """
        self.__height = self.hw_validator("height", value)

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        """
        self.__x = self.xy_validator("x", value)

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        """
        self.__y = self.xy_validator("y", value)

    def hw_validator(self, name, value):
        """
        Raises: TypeError if Value is not int
                ValueError if value <=0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 1:
            raise ValueError("{:s} must be > 0".format(name))
        return value

    def xy_validator(self, name, value):
        """
        Raises: TypeError if Value is not int
                ValueError if value <=0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0:
            raise ValueError("{:s} must be >= 0".format(name))
        return value

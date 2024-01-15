#!/usr/bin/python3
"""
A module Defining the "Base" class
"""

import csv
import json
import turtle


class Base:
    """Representation of A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """This returns the JSON string that represents a list of
        dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """This returns the JSON list string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """This writes the JSON string representation of list_objs
        to a file"""
        name_file = cls.__name__ + ".json"
        t = []
        if list_objs is not None:
            for x in list_objs:
                t.append(cls.to_dictionary(x))
        with open(name_file, 'w') as f:
            f.write(cls.to_json_string(t))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            d = cls(1, 1)
        elif cls.__name__ == "Square":
            d = cls(1)
        d.update(**dictionary)
        return d

    @classmethod
    def load_from_file(cls):
        name_file = cls.__name__ + ".json"
        y = []
        try:
            with open(name_file, 'r') as f:
                y = cls.from_json_string(f.read())
            for x, e in enumerate(y):
                y[x] = cls.create(**l[x])
        except:
            pass
        return y

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A list of Rectancle is serialized in csv"""
        nom_file = cls.__name__ + ".csv"
        with open(nom_file, 'w', newline='') as csvfile:
            writes_csv = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writes_csv.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writes_csv.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv"""
        nom_file = cls.__name__ + ".csv"
        y = []
        try:
            with open(filename, 'r') as csvfile:
                reads_csv = reads.csv(csvfile)
                for args in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    y.append(obj)
        except:
            pass
        return y

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        width_screen = 620
        padding = 10
        width_row = padding
        height_row = 0
        height_screen = padding
        color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo',
                      'violet']
        size_color = len(color_list)
        index_color = 0
        for rectangle in list_rectangles:
            rect_potential_width = width_row + rectangle.width + rectangle.x
            + padding
            if (width_row == padding or rect_potential_width < width_screen):
                width_row += rectangle.width + rectangle.x + padding
                if (height_row < rectangle.height + rectangle.y):
                    height_row = rectangle.height + rectangle.y
            else:
                height_screen += height_row + padding
                width_row = rectangle.width + rectangle.x + padding * 2
                height_row = rectangle.height + rectangle.y

        for sqr in list_squares:
            potential_width = width_row + sqr.size + sqr.x + padding
            if (width_row == padding or potential_width < width_screen):
                width_row += sqr.size + sqr.x + padding
                if (height_row < sqr.size + sqr.y):
                    height_row = sqr.size + sqr.y
            else:
                height_screen += height_row + padding
                width_row = sqr.size + sqr.x + padding * 2
                row_height = sqr.size + sqr.y
        turtle.screensize(canvwidth=width_screen, canvheight=height_screen)
        turtle.pu()
        turtle.left(180)
        turtle.forward(width_screen/2 - padding)
        turtle.right(90)
        turtle.forward(height_screen/2 - padding)
        turtle.right(90)
        width_row = padding
        height_row = 0
        for rect in list_rectangles:
            potential_width = width_row + rectangle.width + rectangle.x
            + padding
            if (width_row == padding or potential_width < width_screen):
                width_row += rectangle.width + rectangle.x + padding
                if (height_row < rectangle.height + rectangle.y):
                    height_row = rectangle.height + rectangle.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(width_row - padding)
                turtle.left(90)
                turtle.forward(height_row + padding)
                turtle.left(90)
                width_row = rectangle.width + rectangle.x + padding * 2
                height_row = rectangle.height + rectangle.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(rect.x)
            turtle.right(90)
            turtle.forward(rect.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.right(90)
                turtle.forward(rectangle.height)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(rectangle.width + padding)
            turtle.left(90)
            turtle.forward(rectangle.y)
            turtle.right(90)

        for sqr in list_squares:
            potential_width = row_width + sqr.size + sqr.x + padding
            if (width_row == padding or potential_width < width_screen):
                width_row += sqr.size + sqr.x + padding
                if (height_row < sqr.size):
                    height_row = sqr.size + sqr.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(width_row - padding)
                turtle.left(90)
                turtle.forward(height_row + padding)
                turtle.left(90)
                width_row = sqr.size + sqr.x + padding * 2
                height_row = sqr.size + sqr.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(sqr.x)
            turtle.right(90)
            turtle.forward(sqr.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(sqr.size)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(sqr.size + padding)
            turtle.left(90)
            turtle.forward(sqr.y)
            turtle.right(90)

        turtle.getscreen()._root.mainloop()

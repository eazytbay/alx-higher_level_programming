#!/usr/bin/python3
"""
This Test is for the Rectangle class
"""

import unittest
import pep8
import inspect
import io
import json
import os
from contextlib import redirect_stdout
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangleDocs(unittest.TestCase):
    """This Tests the style and documentation of the Rectangle class"""
    @classmethod
    def setUpClass(cls):
        """Prepared for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_pep8_conformance_rectangle(self):
        """This Test to check if models/rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors found (and warnings).")

    def test_pep8_conformance_test_rectangle(self):
        """This Test to confirm if tests/test_models/test_rectangle.py
        conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors found (and warnings).")

    def test_module_docstring(self):
        """This Tests for the availability of a module docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """This Tests for the availability of a docstring class"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """This Tests for the availability of docstrings in all functions"""
        for perf in self.rect_funcs:
            self.assertTrue(len(perf[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    """Test the functionality of the Rectangle class"""
    @classmethod
    def setUpClass(cls):
        """"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(5, 6, 7, 8, 9)
        cls.r4 = Rectangle(11, 12, 13, 14)

    def test_id(self):
        """This Tests for ID functionality"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 9)
        self.assertEqual(self.r4.id, 3)

    def test_width(self):
        """This Test for width functionality"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 5)
        self.assertEqual(self.r4.width, 11)

    def test_height(self):
        """This Tests for height functionality"""
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r3.height, 6)
        self.assertEqual(self.r4.height, 12)

    def test_x(self):
        """This Test for x functionality"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r3.x, 7)
        self.assertEqual(self.r4.x, 13)

    def test_y(self):
        """This Test for y functionality"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 8)
        self.assertEqual(self.r4.y, 14)

    def test_mandatory_width(self):
        """This Tests if width is a mandatory arg"""
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_mandatory_height(self):
        """This Tests if height is a mandatory arg"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1)

    def test_width_typeerror(self):
        """This Test non-ints for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle("hello", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle(True, 1)

    def test_height_typeerror(self):
        """This Test non-ints for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(1, True)

    def test_x_typeerror(self):
        """This Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(1, 1, True)

    def test_y_typeerror(self):
        """This Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(1, 1, 1, True)

    def test_width_valueerror(self):
        """This Test if ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect = Rectangle(0, 1)

    def test_height_valueerror(self):
        """This Test if ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect = Rectangle(1, 0)

    def test_x_valueerror(self):
        """This Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """This Test if ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """The test area"""
        self.assertEqual(self.r1.area(), 100)
        self.assertEqual(self.r2.area(), 6)
        self.assertEqual(self.r3.area(), 30)
        self.assertEqual(self.r4.area(), 132)

    def test_area_args(self):
        """This Tests for too many args for area()"""
        with self.assertRaises(TypeError):
            rect = self.r1.area(1)

    def test_basic_display(self):
        """ This Tests display without x and y"""
        rect = Rectangle(2, 3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 10 + "\n") * 10)
        with io.StringIO() as buf, redirect_stdout(buf):
            rect.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n") * 3)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.r1.display(1)

    def test_str(self):
        """This Test the __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")
        self.assertEqual(str(self.r3), "[Rectangle] (9) 7/8 - 5/6")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 13/14 - 11/12")

    def test_display_xy(self):
        """Checking and Testing the display method with x and y"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r2.display()
            result = buf.getvalue()
            self.assertEqual(rersult, (" " * 4 + "#" * 2 + "\n") * 3)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.r3.display()
            result = buf.getvalue()
            self.assertEqual(result, "\n" * 8 +
                             (" " * 7 + "#" * 5 + "\n") * 6)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.r4.display()
            result = buf.getvalue()
            self.assertEqual(result, "\n" * 14 +
                             (" " * 13 + "#" * 11 + "\n") * 12)

    def test_update_args(self):
        """Checking and Testing the udpate method with *args"""
        rect = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 0/0 - 1/1")
        rect.update(89)
        self.assertEqual(str(rect), "[Rectangle] (89) 0/0 - 1/1")
        rect.update(89, 2)
        self.assertEqual(str(rect), "[Rectangle] (89) 0/0 - 2/1")
        rect.update(89, 2, 3)
        self.assertEqual(str(rect), "[Rectangle] (89) 0/0 - 2/3")
        rect.update(89, 2, 3, 4)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/0 - 2/3")
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_setter(self):
        """Checks if the update method uses setter with *args"""
        rect = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.update(1, 1, 1, 1, -1)

    def test_update_too_many_args(self):
        """This tests too many args for update"""
        rect = Rectangle(1, 1, 0, 0, 1)
        rect.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(rect), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """This test no args for update"""
        rect = Rectangle(1, 1, 0, 0, 1)
        rect.update()
        self.assertEqual(str(rect), "[Rectangle] (1) 0/0 - 1/1")

    def test_update_kwargs(self):
        """Checking and Testing the update method with **kwargs"""
        rect = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 0/0 - 1/1")
        rect.update(height=10)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/10")
        rect.update(width=11, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 11/10")
        rect.update(y=3, width=4, x=5, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 5/3 - 4/10")
        rect.update(x=6, height=7, y=8, width=9)
        self.assertEqual(str(rect), "[Rectangle] (89) 6/8 - 9/7")

    def test_update_kwargs_setter(self):
        """This tests to confirm that the update method uses
        setter with **kwargs"""
        rect = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect.update(width="hello")
        with self.assertRaises(TypeError):
            rect.update(height="hello")
        with self.assertRaises(TypeError):
            rect.update(x="hello")
        with self.assertRaises(TypeError):
            rect.update(y="hello")
        with self.assertRaises(ValueError):
            rect.update(width=-1)
        with self.assertRaises(ValueError):
            rect.update(width=0)
        with self.assertRaises(ValueError):
            rect.update(height=-1)
        with self.assertRaises(ValueError):
            rect.update(height=0)
        with self.assertRaises(ValueError):
            rect.update(x=-1)
        with self.assertRaises(ValueError):
            rect.update(y=-1)

    def test_mix_args_kwargs(self):
        """This tests to confirm the output for mixed args and kwargs"""
        rect = Rectangle(1, 1, 0, 0, 1)
        rect.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(rect), "[Rectangle] (2) 2/2 - 2/2")

    def test_extra_kwargs(self):
        """This tests for random kwargs"""
        rect = Rectangle(1, 1, 0, 0, 1)
        rect.update(hello=2)
        self.assertEqual(str(rect), "[Rectangle] (1) 0/0 - 1/1")

    def test_to_dict(self):
        """This tests regular to_dictionary"""
        d1 = self.r1.to_dictionary()
        self.assertEqual({"id": 1, "width": 10, "height": 10, "x": 0, "y": 0},
                         d1)
        d2 = self.r2.to_dictionary()
        self.assertEqual({"id": 2, "width": 2, "height": 3, "x": 4, "y": 0},
                         d2)
        d3 = self.r3.to_dictionary()
        self.assertEqual({"id": 9, "width": 5, "height": 6, "x": 7, "y": 8},
                         d3)
        d4 = self.r4.to_dictionary()
        self.assertEqual({"id": 3, "width": 11, "height": 12, "x": 13,
                          "y": 14}, d4)
        self.assertTrue(type(d1) is dict)
        self.assertTrue(type(d2) is dict)
        self.assertTrue(type(d3) is dict)
        self.assertTrue(type(d4) is dict)
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(**d4)
        self.assertEqual(str(rect), str(self.r4))
        self.assertNotEqual(rect, self.r4)

    def test_save_to_file(self):
        """This tests the consistency in the use of save_to_file"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        l = [r1, r2]
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            ls = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_stf_empty(self):
        """This tests the save_to_file with an empty list"""
        l = []
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_stf_None(self):
        """test save_to_file with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_create(self):
        """test normal use of create"""
        r1 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        r2 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        r1c = Rectangle.create(**r1)
        r2c = Rectangle.create(**r2)
        self.assertEqual("[Rectangle] (2) 4/0 - 2/3", str(r1c))
        self.assertEqual("[Rectangle] (9) 7/8 - 5/6", str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)

    def test_load_from_file_no_file(self):
        """Checks use of load_from_file with no file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_empty_file(self):
        """Confirms the use of load_from_file with empty file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """This tests the normal use of load_from_file"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        si = [r1, r2]
        Rectangle.save_to_file(si)
        so = Rectangle.load_from_file()
        self.assertTrue(type(so) is list)
        self.assertEqual(len(so), 2)
        r1c = so[0]
        r2c = so[1]
        self.assertTrue(type(r1c) is Rectangle)
        self.assertTrue(type(r2c) is Rectangle)
        self.assertEqual(str(r1), str(r1c))
        self.assertEqual(str(r2), str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)

#!/usr/bin/python3
"""Documentation for classes representing a singly linked list"""


class Node():
    """Class representing a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a node with provided data and an optional next node
        Args:
            data (int): Data to be stored in the node
            next_node (Node, optional): Reference to the next node in the list
        Raises:
            TypeError: Should in case data is not an integer or next_node is not a Node instance
        """

        if type(data) != int:
            raise TypeError("Data must be an integer")
        self.__data = data

        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """Retrieve the data stored in the current node
        Returns:
            int: Data value in the current node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value in the current node
        Args:
            value (int): New data value for the node
        Raises:
            TypeError: If the provided value is not an integer
        """
        if type(value) != int:
            raise TypeError("Data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the list
        Returns:
            Node: Reference to the next node in the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set a new next node for the current node
        Args:
            value (Node): Reference to the new next node
        Raises:
            TypeError: If the provided value is not a Node instance
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """Class representing a singly linked list"""

    def __init__(self):
        """Initialize an empty singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a node into the linked list in sorted order
        Args:
            value (int): Value to be inserted into the linked list
        Raises:
            TypeError: If the provided value is not an integer
        """
        if type(value) != int:
            raise TypeError("Data must be an integer")

        ephem = None
        iterator = self.__head
        new_node = Node(value)

        if iterator is None:
            new_node.next_node = None
            self.__head = new_node
        else:
            while iterator is not None and value > iterator.data:
                ephem = iterator
                iterator = iterator.next_node

            if ephem is None:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                ephem.next_node = new_node
                new_node.next_node = iterator

    def __str__(self):
        """Return a string representation of the linked list"""
        linked_list = []
        iterator = self.__head

        while iterator is not None:
            linked_list.append(iterator.data)
            iterator = iterator.next_node

        return '\n'.join(str(x) for x in linked_list)

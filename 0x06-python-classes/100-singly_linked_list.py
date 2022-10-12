#!/usr/bin/python3
"""
Singly Linked List Module
"""


class Node:
    """
    Checks the current node position
    """

    def __init__(self, data, next_node=None):
        """
        Instance initialization
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter Function"""
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter Function """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Next Node Getter """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Next Node Setter """
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Defines a singly linked list """

    def __init__(self):
        """ Initializes singly linked list """
        self.__head = None

    def __str__(self):
        """ Represent Singly Linked List as strings to be printed """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """ Inserts new Nodes into singly linked list in sorted order """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return
        while (tmp.next_node is not None) and (new.data > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return

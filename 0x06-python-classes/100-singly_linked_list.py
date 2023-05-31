#!/usr/bin/python3
"""two classes as linklist node and singlylinkedlist
    help to form data structure of single link list
"""


class Node:
    """class node that act as node of link list
        form of data and next_node arretibutes
    """
    def __init__(self, data, next_node=None):
        """init of instance of new node with two attr
            Args:
                data: value of data attribute
                next_node: value of next node
            Attr:
                data: instance private attr of data
                next_node: instance private attr of next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter of data attr which is number only
            Returns:
                data value of node
        """
        return self.__data

    @property
    def next_node(self):
        """getter of next node which should be Node Instance
            Returns:
                Node instance next in list
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """setter of data attr anf check if int or not
            Args:
                value: value of data attr enter in new node
            Raises:
                TypeError: if value is not int type
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """next_node setter attr check if next_node is
            Node instance or None value only
            Args:
                value: next_node attr value
            Raises:
                TypeError: if not instance of class node or none
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """class identify single link list and intiate it
        contain insterted new item and print its result
    """
    def __init__(self):
        """init of instance of new link list
            with head of new list
            Attr:
                head: head of list, it be None at first
        """
        self.__head = None

    def sorted_insert(self, value):
        """ methode add node to list sorted accord
            data inside list nodes in begin or at end or
            in middle of list
            Args:
                Value: value of data of new node inserted in list
        """
        if not self.__head:
            self.__head = Node(value)
        else:
            ptr = self.__head
            while ptr:
                if value > ptr.data and ptr.next_node:
                    if value < ptr.next_node.data:
                        ptr.next_node = Node(value, ptr.next_node)
                        break
                    else:
                        pass
                if value > ptr.data and ptr.next_node is None:
                    ptr.next_node = Node(value)
                    break
                if value < ptr.data:
                    self.__head = Node(value, self.__head)
                    break
                if value == ptr.data:
                    ptr.next_node = Node(value, ptr.next_node)
                    break
                ptr = ptr.next_node

    def __str__(self):
        """convert object to string to be able printed in print
            function
            Returns:
                string of object or nothing if empty
        """
        obj_str = ""
        if not self.__head:
            return obj_str
        else:
            temp = self.__head
            while temp:
                if not temp.next_node:
                    obj_str += str(temp.data)
                else:
                    obj_str += str(temp.data) + "\n"
                temp = temp.next_node
            return obj_str

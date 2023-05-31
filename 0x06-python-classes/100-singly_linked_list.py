#!/usr/bin/python3
"""two classes as linklist node and singlylinkedlist"""


class Node:
    """class node that act as node of link list"""
    def __init__(self, data, next_node=None):
        """init of instance
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
        """getter of data attr
            Returns:
                data value
        """
        return self.__data

    @property
    def next_node(self):
        """getter of next node
            Returns:
                next_node value
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """setter of data attr
            Args:
                value: value of data attr
            Raises:
                TypeError: if not int type
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """next_node setter attr
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
    """class identify single link list"""
    def __init__(self):
        """init of instance
            Attr:
                head: head of list
        """
        self.__head = None

    def sorted_insert(self, value):
        """ methode add node to list sorted accord
            data inside list nodes
            Args:
                Value: value of node inserted
        """
        if not self.__head:
            self.__head = Node(value)
        else:
            ptr = self.__head
            while ptr:
                if value > ptr.data and
                ptr.next_node and value < ptr.next_node.data:
                    ptr.next_node = Node(value, ptr.next_node)
                    break
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
        """convert object as string
            Returns:
                string of object
        """
        if not self.__head:
            return
        else:
            obj_str = ""
            temp = self.__head
            while temp:
                if not temp.next_node:
                    obj_str += str(temp.data)
                else:
                    obj_str += str(temp.data) + "\n"
                temp = temp.next_node
            return obj_str

#!/usr/bin/python3


class Node:

    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node

    @property
    def data(self):

        return (self.__data)

    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):

        if not isinstance(value, Node) and value is not None:

            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:

    def __init__(self):

        self.__head = None

    def sorted_insert(self, value):

        newvalue = Node(value)

        if self.__head is None:
            newvalue.next_node = None
            self.__head = newvalue

        elif self.__head.data > value:

            newvalue.next_node = self.__head
            self.__head = newvalue

        else:
            tmpvalue = self.__head

            while (tmpvalue.next_node is not None and
                    tmpvalue.next_node.data < value):

                tmpvalue = tmpvalue.next_node
            newvalue.next_node = tmpvalue.next_node

            tmpvalue.next_node = newvalue

    def __str__(self):

        valuess = []

        tmpvalue = self.__head

        while tmpvalue is not None:

            valuess.append(str(tmpvalue.data))
            tmpvalue = tmpvalue.next_node

        return ('\n'.join(valuess))

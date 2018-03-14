#
#
#
# The ADT module provides support for specifying algebraic data types for Nagini.
# ADTs are meant to be used exclusively in contracts: although they are syntatically
# correct Python constructs, they should be defined with no functional intent while
# running the code. Still, Nagini will semantically consider it while verifying the
# code.
#
# Example: linked list
#
# Pseudo-code:
#
#    LinkedList = Null
#               | Node(elem: int, next: LinkedList)
#
# Python definition: 
#
#   class LinkedList(ADT):
#       pass
#   
#   class Node(LinkedList, NamedTuple('Node', [('elem', int), ('next', LinkedList)])):
#       pass
#   
#   class Null(LinkedList, NamedTuple('Null', [])):
#       pass
#
# Uses:
#
#   list_1 = Null()                         []
#   list_2 = Node(2, Null())                [2]
#   list_3 = Node(3, Node(4, Null()))       [3, 4]
#

class ADT:
    pass

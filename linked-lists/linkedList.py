# https://www.geeksforgeeks.org/linked-list-vs-array/
# https://zippy-lan-200.notion.site/Intro-to-Linked-Lists-2ea969ab51874fb688d15973ffa12a61

from readline import insert_text


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

new_node = Node(5)

# print(new_node)
# print(new_node.value)
# print(new_node.next)
class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def pushOn(self, new_value):
        new_node = Node(new_value, self.head)
        self.head = new_node

    def append(self, new_value):
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
        
        last = self.head

        while last.next:
            # print("+++++++++++++")
            # print(f'Current Node: {last}')
            # print(f'Current Value: {last.value}')
            # print(f'Current next: {last.next}')
            last = last.next
            # print('+++++++++++++')
            # print(f'New node is at:{last}')
        last.next = new_node

    def traverse(self):
        if self.head is None or self.head.next is None:
            return self.head

        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def insertAfter(self, prev_node, value):
        if prev_node is None:
            print('Hey, that Node doesnt exist here!')
            return
        
        new_node = Node(value)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def removeDupsSorted(self):
        temp = self.head
        while temp:
            while temp.next and temp.next.value == temp.value:
                temp.next = temp.next.next
            temp = temp.next
        return self.head
    
    def removeDups(self):
        if self.head is None:
            return self.head
        values = set()
        values.add(self.head.value)

        temp = self.head
        while temp and temp.next:
            if temp.next.value in values:
                temp.next = temp.next.next
            else:
                values.add(temp.next.value)
                temp = temp.next
        return self.head


my_list = LinkedList()

my_list.pushOn('Nate')
my_list.pushOn("Billy")
my_list.append('Coding Temple')
my_list.traverse()
print('______________')
my_list.insertAfter(my_list.head.next, 'ALumni Workshop')
my_list.traverse()



    


# linked_list = LinkedList()



# https://www.geeksforgeeks.org/linked-list-vs-array/
# https://zippy-lan-200.notion.site/Intro-to-Linked-Lists-2ea969ab51874fb688d15973ffa12a61

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
            print("+++++++++++++")
            print(f'Current Node: {last}')
            print(f'Current Value: {last.value}')
            print(f'Current next: {last.next}')
            last = last.next
            print('+++++++++++++')
            print(f'New node is at:{last}')
        last.next = new_node

    

    


        
        

my_list = LinkedList()

my_list.pushOn('Nate')
my_list.pushOn("Billy")
my_list.append('Coding Temple')




    


# linked_list = LinkedList()



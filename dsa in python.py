# exp = [2200, 2350, 2600, 2130, 2190]
# print("extra money spent on feb is :", exp[1] - exp[0])
# print("total expenses in first quarter",exp[0]+exp[1]+exp[2])
# print("did i spend any 2000$ in any month:" , 2000 in exp)
# exp.append(1980)
# print(exp)
# exp[3] = exp[3] - 200
# print(exp)
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data)  + suffix
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)



if __name__ == '__main__':
    root = linkedlist()
    root.insert_at_beginning(5)
    root.insert_at_beginning(10)
    root.insert_at_beginning(15)
    root.insert_at_end(234) 
    root.print()
# 22:06 se dekhna h
        
        


        
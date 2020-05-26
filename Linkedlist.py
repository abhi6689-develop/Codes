class Node: #Nodes are the basically the placeholders for the elements of the linkedlist
    def __init__(self, data): #
        self.data = data #Each node has a value stored in it, you pass ther value by creating an object 
        self.next = None #It also has a pointer that points to the next node, here that pointer points to nothing 

class LinkedList:
    def __init__(self):
        self.head = None 
        
    def push(self,new_data): #adding a node at the beginning of the linkedlist 
        new_node = Node(new_data) #making a new node for the data 
        new_node.next = self.head #making the next of the new node point to the head of the linkedlist 
        self.head = new_node
        
    def insert_after_a_node(self, prev_node, new_data): #adding a node after another node in the linkedlist 

        if prev_node is None: #In this case, the new node cant be the head 
            print("Yaha nai daal sakta behnchod")
            return 
        new_node = Node(new_data) #making a node for the data
        new_node.next = prev_node.next #making the next of the new node point to the next of the prevoius node 
        prev_node.next = new_node  #Now make the previous node point to the new node 
    
    def insert_at_last(self, new_data):
        
        new_node = Node(new_data) #making a node for the data 
        if self.head is None: #check if the linkedlist is empty 
            new_node = self.head #we insert the new node as the head 
            return 
        else:  #if the list is not empty, start traversing the linkedlist
            end = self.head  #it starts from the head of the linkedlist 
            while end.next:  #traversing till we reach the second last node 
                end = end.next  #Accessing the last node 
            end.next = new_node  #adding the new node after the last node 

    def delete_given_a_key(self, key):

        temp = self.head #initialise temp at the head 
        if temp is not None: #check that the list is not empty 
            if temp.data == key: #If the head is the data to be removed
                self.head = temp.next #move the head, to the next node
                temp = None  #remove the node 
                return
        while temp: #You go till the last element 
            if temp.data == key: #If you find the data to be deleted 
                break #Stop there 
            prev = temp #Make the current node the previous node before moving on to the next node 
            temp = temp.next #Go to the next node 
        if temp == None:
            return "Key not present in the list"
        prev.next = temp.next #link the previous node to the next node 
        temp = None #Remove the current node 

    def deleting_given_position(self, position):
            temp = self.head 
            if temp is not None: #checks that the list is not empty 
                if position == 0:
                    self.head = temp.next 
                    temp = None 
                    return
                else:
                    for _ in range(position):
                        prev = temp 
                        temp = temp.next 
                    prev.next = temp.next 
                    temp = None 

    def delete_linkedlist(self):
        current = self.head 
        while current: 
            prev = current.next
            current.data = None 
            current = prev  

    def length_of_list(self):
        temp = self.head 
        count = 1 
        while temp.next:
            temp = temp.next 
            count += 1 
        return count 
    
    def search_for_an_element(self, search_element):
        current = self.head 
        count = 0 
        if current.data == search_element:
            print(current.data, "found at position", count)
        else:
            while current:
                current = current.next 
                count += 1 
                if current.data == search_element:
                    break 
            print(current.data, "found at position", count)

    def return_nth_node(self,nth_node):
        current = self.head
        for _ in range(nth_node):
            current = current.next 
        return current.data

    def return_middle(self):
        count = 1 
        temp = self.head 
        while temp.next:
            temp = temp.next
            count += 1 
        print(count)
        temp = self.head
        for _ in range(count//2):
            temp = temp.next 
        return temp.data 

    def node_count(self, new_data):
        count = 0 
        temp = self.head
        while temp:
            if temp.data == new_data:
                count+= 1 
            temp = temp.next 
        
        return count

    def find_a_loop(self):
        table = []
        temp = self.head
        while temp: 
            temp = temp.next 
            if temp in table:
                print("Loop found")
                return True
            table.append(temp)
        print("No loop found")
        return False 

    def finding_length_of_loop(self):
        table = []
        temp = self.head 
        count = 0 
        while temp:
            count += 1
            temp = temp.next
            if temp in table:
                print("loop found")
                print(abs(table.index(temp)+1-count))
                return True 
            table.append(temp)
        print("No loop found")
        return False 
    
    def is_palindrome(self):
        table = []
        elbat = []
        temp = self.head 
        while temp:
            table.append(temp.data)
            temp = temp.next 
        for i in range(len(table)-1, -1, -1):
            elbat.append(table[i])
        print(table)
        print(elbat)
        if table == elbat:
            return True
        else:
            return False 

    def delete_duplicate_node(self):
        temp = self.head
        while temp:
            prev = temp
            temp = temp.next 
            if prev.data == temp.data:
                prev.next = temp.next.next
                temp = None 

    def delete_duplicate_node_unsorted(self):
        temp = self.head 
        stack = []
        while temp:
            prev = temp 
            stack.append(prev.data)
            temp = temp.next 
            if temp.data in stack:
                prev.next = temp.next.next
                temp = None 
                
    def swap_nodes(self, x, y):
        current_x = self.head 
        prev_x = None 
         
        while current_x and current_x.data != x:
            prev_x = current_x
            current_x = current_x.next 
        
        current_y = self.head 
        prev_y = None 
        
        while current_y and current_y.data != y:
            prev_y = current_y
            current_y = current_y.next 
        
        if current_x == current_y == None:
            return 

        if prev_x != None:
            prev_x.next = current_y
        else:
            self.head = current_y
        
        if prev_y != None:
            prev_y.next = current_x
        else:
            self.head = current_x


        temp = current_x.next
        current_x.next = current_y.next 
        current_y.next = temp 
    
    def pairwise_swap(self):
        temp = self.head 
        while temp.next:
            temp.data, temp.next.data = temp.next.data, temp.data 
            temp = temp.next.next 


                
        
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next 



if __name__ == "__main__":

    llist = LinkedList() 
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    llist.printlist()
    print()
    llist.pairwise_swap()
    print()
    llist.printlist()
 

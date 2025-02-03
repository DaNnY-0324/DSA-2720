from Lab2_singly_linked_list import SinglyLinkedList

def main():
    # Create an empty singly linked list
    linked_list = SinglyLinkedList()
    print("Created empty list:", linked_list.display())

    # Insert values at different positions
    print("\nInserting values:")
    linked_list.insert_at_beginning(1)
    print("After inserting 1 at beginning:", linked_list.display())
    
    linked_list.insert_at_end(3)
    print("After inserting 3 at end:", linked_list.display())
    
    linked_list.insert_at_position(2, 1)
    print("After inserting 2 at position 1:", linked_list.display())
    
    # Display list length
    print("\nList length:", linked_list.length)
    
    # Search for values
    print("\nSearching for values:")
    print("Position of 2:", linked_list.search(2))
    print("Position of 4:", linked_list.search(4))
    
    # Find middle element
    print("\nMiddle element:", linked_list.find_middle())
    
    # Reverse the list
    print("\nReversing the list:")
    print("Before reverse:", linked_list.display())
    linked_list.reverse()
    print("After reverse:", linked_list.display())
    
    # Delete a node
    print("\nDeleting node with value 2:")
    linked_list.delete_by_value(2)
    print("After deletion:", linked_list.display())

if __name__ == "__main__":
    main()
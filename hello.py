def create_list():
    return []

def append_to_list(lst, item):
    lst.append(item)
    return lst

def remove_from_list(lst, item):
    if item in lst:
        lst.remove(item)
    else:
        print(f"{item} not found in the list.")
    return lst

def display_list(lst):
    print("Current List:", lst)

def main():
    my_list = create_list()
    
    while True:
        print("\nMenu:")
        print("1. Create a new list")
        print("2. Append an item to the list")
        print("3. Remove an item from the list")
        print("4. Display the list")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            my_list = create_list()
            print("New list created.")
        elif choice == '2':
            item = input("Enter the item to append: ")
            my_list = append_to_list(my_list, item)
            print(f"{item} appended to the list.")
        elif choice == '3':
            item = input("Enter the item to remove: ")
            my_list = remove_from_list(my_list, item)
        elif choice == '4':
            display_list(my_list)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
        main()
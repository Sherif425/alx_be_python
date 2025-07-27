def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print("=======================")
            print(f"{item} added to the list.")
            print("=======================")
           
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print("=======================")
                print(f"{item} removed from the list.")
                print("=======================")
            else:
                print("=======================")
                print(f"{item} not found in the list.")
                print("=======================")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
               print("=======================")
               print(f"Current Shopping List: \n{shopping_list}")
               print("=======================")
            else:
                print("\n=======================")
                print("\nYour shopping list is empty.")
                print("=======================\n")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

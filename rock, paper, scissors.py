choice = ()
while True:
    print("\nRock, Paper, Scissors")
    print("1. Play Game")
    print("2. Exit")
    
    choice = input("Please choose an option ")
    if choice == '1':
        print("Game started")
    elif choice == '2':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again")
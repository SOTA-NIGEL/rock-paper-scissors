data = {}

def collect_incoming_data():
    name = input("Enter your name ")
    age = input("Enter your age ")
    location = input("Enter your location ")
    
    data['name'] = name
    data['age'] = age
    data['location'] = location
    
    print('Data collection succesful')

def display_data():
    print("Collected data: ")
    print("Name: ",data['name'])
    print("Age: ",data['age'])
    print("Location: ",data['location'])

while True:
    print("\nData Collection Program")
    print("1. Collect Data")
    print("2. Display Data")
    print("3. Exit")
    
    choice = input("Plese choose an option ")
    if choice == '1':
        collect_incoming_data()
    elif choice == '2':
        display_data()
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again")   
        
        
        
        
        
        
    
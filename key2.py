import time

def promote_wellness():
    print("Welcome to Wellness Promotion Program!")
    
    while True:
        print("\n1. Get health tips")
        print("2. Relaxation exercise")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            print("Health Tip: Remember to stay hydrated and eat a balanced diet.")
        elif choice == '2':
            print("Relaxation Exercise: Take a deep breath in, hold for a few seconds, and exhale slowly. Repeat.")
        elif choice == '3':
            print("Exiting Wellness Promotion Program. Take care!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
        
        time.sleep(2)  # Add a delay for a better user experience

# Run the wellness promotion program
promote_wellness()

import sys
import main_features.show_bread as main_features_1
import main_features.create_update_bread as main_features_2
import main_features.remove_bread as main_features_3
def login_baker():        
    attempts = 0
    max_attempts = 3
    correct_input = "ahjussi"

    while attempts < max_attempts:
        user_input = input("Enter the correct input (Type 'ahjussi'): ")
        
        if user_input == correct_input:
            print("Correct input! Thank you.")
            break
        else:
            attempts += 1
            print(f"Incorrect input. You have {max_attempts - attempts} attempt(s) remaining.")
            
            if attempts == max_attempts:
                print("Maximum attempts reached. The program will now exit.")
                sys.exit()
    while(True):  
        print("Welcome Ahjussi, please select your desire menu:")
        print("\nList Menu \n1. Show Available Stocks \n2. Add and Edit Stocks \n3. Remove Stocks \n4. Back to menu")
        menu_baker = int(input("Input number: "))    
        if menu_baker == 1:
            main_features_1.show_item()  
        elif menu_baker == 2:
            main_features_2.create_update_item()
        elif menu_baker == 3:
            main_features_3.remove_item()
        elif menu_baker == 4:
            print("See you again!")
            break
        else:
            print("Menu doesn't exist, please input correct number of menu\n")
            continue
import sys
import additional_features.sorted_show_bread as additional_features1
import additional_features.buy_bread as additional_features2

def login_customer():
    while(True):
            print("\n\t\t===EXCLUSIVE OFFER===\nEnjoy a special \"20%\" discount on all our promo items  ")
            print("\nList Menu \n1. Show Bread List \n2. Buy Bread \n3. Exit Program")
            menu = int(input("Enter the menu number to proceed: "))
            if menu == 1:
                additional_features1.sort_item()
            elif menu == 2:
                additional_features2.buy_item()
            elif menu == 3:
                 sys.exit()
            else:
                print("Input invalid. Try again!")
                continue
    
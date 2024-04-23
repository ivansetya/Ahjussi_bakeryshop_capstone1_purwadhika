import user.login_as_baker as baker
import user.login_as_customer as customer


while(True):
    print("\nWelcome to \'Ahjussi Bakery Shop\'")
    print("Login as: ")
    try:
        login = int(input("Enter number user types\n1.) Baker \n2.) Customer \nYour number: "))
        if login == 1:
            baker.login_baker()
        elif login == 2:
            customer.login_customer()
        else:
            print("Please input only 1 or 2")
            continue
    except ValueError:
            print("Invalid input. Please enter a valid input.")
            continue
    

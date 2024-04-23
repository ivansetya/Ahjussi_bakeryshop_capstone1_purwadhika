import bread_collection as stok
import additional_features.handling_inp as handling_inp
from tabulate import tabulate

def buy_item():
    warehouse = stok.warehouse
    total = 0
    cart = []

    print("Bread list: ")
    print(tabulate(warehouse.values(), headers='keys', showindex='always', tablefmt='pretty'))

    while True: 
        choose_index = handling_inp.user_inp_data("Enter the bread index: ", int)
        if choose_index not in warehouse:
            print("Index invalid.")
            continue
    
        quantity = handling_inp.user_inp_data(f"Enter the quantity for {warehouse[choose_index]['name']}: ", int)
        if quantity > warehouse[choose_index]["stock"]:
            print(f"Sorry, we only have {warehouse[choose_index]['stock']} pieces of {warehouse[choose_index]['name']} in stock.")
            if cart:
                print("\nCurrent Cart:")
                cart_table = [["Item", "Quantity", "Price", "Total"]]
                for name, quantity, price in cart:
                    total_price = quantity * price
                    cart_table.append([name, quantity, f"{price:,}", f"{total_price:,}"])
                print(tabulate(cart_table, headers="firstrow", tablefmt="pretty"))
            continue
        
       

        price = warehouse[choose_index]['price']
        if warehouse[choose_index]['promo']:
            price *= 0.8 #Apply 20% discount

        item_name = warehouse[choose_index]['name']
        item_found = False
        for i, (name, existing_quantity, existing_price) in enumerate(cart):
            if name == item_name :
                new_quantity = existing_quantity + quantity
                cart[i] = (name, new_quantity, price)
                item_found = True
                break
     
        if not item_found:
            cart.append((item_name, quantity, price))

        total += quantity * price
        warehouse[choose_index]["stock"] -= quantity

        print("\nShopping Cart:")
        cart_table = [["Item", "Quantity", "Price", "Total"]]
        for name, quantity, price in cart:
            total_price = quantity * price
            cart_table.append([name, quantity, f"{price:,}", f"{total_price:,}"])
        print(tabulate(cart_table, headers="firstrow", tablefmt="pretty"))

        choice = handling_inp.user_inp_opt("Buy again(yes/no): ", ["yes", "no"]).lower()
        if choice != 'yes':
            break

    print(f"\nTotal Price : IDR {total:,}")
    while True:
        try:
            paid = handling_inp.user_inp_data("Thankyou!, insert your cash : ", int)
            change = paid - total
            if paid >= total:
                print(f"Your change : IDR {change:,}")
                break
            else:
                print(f"Your cash is not enough : IDR {abs(change):,}")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid input.")
            continue
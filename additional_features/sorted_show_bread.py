import bread_collection as stok
import main_features.show_bread as main_features_1
from tabulate import tabulate

def sort_item():
    warehouse_list = list(stok.warehouse.items())

    while True:
        print("\nSorted and Filter Menu\n1.) Show All Menu\n2.) Filter by Promo\n3.) Sorted by Highest Stocks\n4.) Sorted by Highest Price\n5.) Back to Menu\n")
        input_menu = input("Enter desired number menu: ")

        if input_menu == "1":
            main_features_1.show_item()
        elif input_menu == "2":
            sorted_by_stock = sorted(warehouse_list, key=lambda x: x[1]['stock'], reverse=True)
            promo_items = [item for item in sorted_by_stock if item[1]['promo']]
            headers = ['Key', 'Name', 'Stock', 'Price', 'Promo']
            rows = [[key, value['name'], value['stock'], value['price'], value['promo']] for key, value in promo_items]
            print(tabulate(rows, headers=headers, tablefmt='pretty'))
        elif input_menu == "3":
            sorted_by_stock = sorted(warehouse_list, key=lambda x: x[1]['stock'], reverse=True)
            headers = ['Key', 'Name', 'Stock', 'Price', 'Promo']
            rows = [[key, value['name'], value['stock'], value['price'], value['promo']] for key, value in sorted_by_stock]
            print(tabulate(rows, headers=headers, tablefmt='pretty'))
        elif input_menu == "4":
            sorted_by_price = sorted(warehouse_list, key=lambda x: x[1]['price'], reverse=True)
            headers = ['Key', 'Name', 'Stock', 'Price', 'Promo']
            rows = [[key, value['name'], value['stock'], value['price'], value['promo']] for key, value in sorted_by_price]
            print(tabulate(rows, headers=headers, tablefmt='pretty'))
        elif input_menu == "5":
            break
        else:
            print("Number menu doesn't exist")
            continue




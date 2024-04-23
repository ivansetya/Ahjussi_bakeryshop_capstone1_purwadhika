import bread_collection as stok
from tabulate import tabulate

def show_item():
    warehouse = stok.warehouse
    print("Bread list\n")
    print(tabulate(warehouse.values(),headers='keys', showindex='always',tablefmt='pretty'))

import bread_collection as stok

def remove_item():
    warehouse = stok.warehouse
    while True:
        pilih_daftar = int(input("Enter bread index that want to remove: "))
        if pilih_daftar not in warehouse:
            print("Data not exist\n")
        else:
            print(f"{warehouse[pilih_daftar]['name']} successfully removed")
            del warehouse[pilih_daftar]
            break
            
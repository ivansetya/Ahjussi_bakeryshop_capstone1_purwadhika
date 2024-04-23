import bread_collection as stok
import additional_features.handling_inp as handling_inp

def create_update_item():
    warehouse = stok.warehouse
    input_baker_bread_name = input("Enter your bread name: ").title()

    #update stock in the warehouse
    for bread in warehouse.values():        
        if bread['name'] == input_baker_bread_name:
            update_oven_bread_stock = handling_inp.user_inp_data("Enter the new bread stock: ", int)
            update_oven_bread_price = handling_inp.user_inp_data("Enter the new bread price: ", int)
            update_promo_sales = handling_inp.user_inp_opt("Do you want to add promo for these item?(yes/no): ", ["yes", "no"]).lower()
            bread['stock'] = update_oven_bread_stock
            bread['price'] = update_oven_bread_price
            bread['promo'] = bool(update_promo_sales == "yes")
            print(f"\n{input_baker_bread_name} has been updated with {update_oven_bread_stock} stock and {update_oven_bread_price} price.")
            return
    
   
    input_oven_bread_stock = handling_inp.user_inp_data("Enter your bread stock: ", int)
    input_oven_bread_price = handling_inp.user_inp_data("Enter your bread price: ", int)
    input_promo_sales = handling_inp.user_inp_opt("Do you want to add promo for these item?(yes/no): ", ["yes", "no"]).lower()     
    warehouse[int(len(warehouse))] = ({
                'name'  : input_baker_bread_name,
                'stock' : input_oven_bread_stock,
                'price' : input_oven_bread_price,
                'promo' : bool(input_promo_sales) == "yes"})
    print(f"\n{input_baker_bread_name} has been added with {input_oven_bread_stock} stock and {input_oven_bread_price} price")


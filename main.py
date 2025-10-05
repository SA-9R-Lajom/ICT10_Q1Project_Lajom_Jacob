from pyscript import display
#Resturant Order System 

resturant name= "Midnight Tokyo Brewery"
owner_name= "Jake Marshall"

year_since_opened= "1989"

tax_rate ="0.08"

has_delivery= "True"
is_dine_in = "True"
is_take_out = "True"
is_open_247 ="false"

product_names " = ["Spaghetti Bolognese", "California Maki Sushi", "Caesar Salad"]
beverages = ["Iced Tea", "Soda"]

buisness_hours = "7:00 AM - 12:00 PM"

menu {

    "Spaghetti Bolognese": 12.99,
    "California Maki Sushi": 9.99,
    "Caesar Salad": 7.99,
    "Iced Tea": 2.50,
    "Soda": 1.99
}

common_allergens = ["Gluten", "Dairy", "Nuts", "Soy"]

display(resturant_name, target="name1")
display(owner_name, target="owner")
display(year_since_opened, target="year")

display(product_names[0], target="item1")
display(f"${menu['Spaghetti Bolognese']:.2f}", target="price1")
display(product_names[1], target="item2")
display(f"${menu['California Maki Sushi']:.2f}", target="price2")
display(product_names[2], target="item3")
display(f"${menu['Caesar Salad']:.2f}", target="price3")
display(beverages[0], target="drink1")
display(f"${menu['Iced Tea']:.2f}", target="drinkprice1")
display(beverages[1], target="drink2")
display(f"${menu['Soda']:.2f}", target="drinkprice2")

display(f"Open: {buisness_hours[0]} - business_hours[1]}", target="openinghours")

dipslay(f"Dine-in & TakeOut Available", target="orderType")
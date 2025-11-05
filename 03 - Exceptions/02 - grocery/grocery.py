grocery_list = {}
item_counter = 1

while True:
    try:
        grocery_item = input()
    except EOFError:
        break
    
    if grocery_item in grocery_list:
        item_counter += 1
        grocery_list[grocery_item] = item_counter
    else:
        grocery_list[grocery_item] = 1
    
for  item, quantity in sorted(grocery_list.items()):
    print(quantity, item.upper())


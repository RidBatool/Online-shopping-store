# Importing the view_cart function to display the user's cart
from view_cart import view_cart

# Function to remove items from the user's cart
def remove_from_cart(user_id):
    # Display the user's current cart
    view_cart(user_id)

    # Read the content of the user's cart file
    with open(f'{user_id}_cart.txt', 'r') as file:
        content = file.read()[:-1]

    list_strings = content.split('\n')
    main_list = []

    # Convert the string representations of lists to actual lists
    for i in list_strings:
        list_item = eval(i)
        main_list.extend([list_item])

    while True:
        item = input("Enter the item you want to remove (First letter of your item name should be capital) and if you complete removing item press 'e'\n")
        count = 0

        if item == 'e':
            # Update the user's cart file with the modified cart content
            with open(f'{user_id}_cart.txt', 'w') as file:
                for i in main_list:
                    file.write(f"{str(i)}" + '\n')
                break
        else:
            for i in main_list:
                count = 0
                if item == i[0]:
                    count += 1
                    quantity = int(input("Enter the quantity you want to remove:\n"))

                    # Read the product information from the product file
                    with open('product.txt', 'r') as file:
                        items = [line.strip().split(':') for line in file]

                    for product_info in items:
                        if product_info[0] == i[0]:
                            price = int(product_info[1]) * quantity
                            previous_quantity = int(i[1])
                            previous_price = int(i[2])

                            new_quantity = previous_quantity - quantity
                            new_price = previous_price - price

                            if new_quantity == 0:
                                main_list.remove(i)
                            else:
                                i[1] = str(new_quantity)
                                i[2] = str(new_price)

            if count < 0:
                print("Item not Found")


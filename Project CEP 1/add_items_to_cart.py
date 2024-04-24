# Function to add items to the user's shopping cart
def add_items_to_cart(user_id):
    main_list = []  # List to store items in the cart
    cart = load_cart(user_id)  # Load existing items in the cart
    items = load_items()  # Load available items from the product list

    while items:
        # Display available items
        print("\nAvailable Items:")
        for item in items:
            print(f'{item[0]} - Price: {item[1]}')

        user_input = input('\nEnter the items you want to add (or "e" to exit): ').lower()

        if user_input.lower() == 'e':
            break

        # Find the selected item in the available items
        selected_item = next(
            (item for item in items if user_input.lower() == item[0].lower()),
            None)

        if selected_item:
            # Prompt the user for the quantity of the selected item
            quantity = int(input(f'Enter the quantity of {selected_item[0]} you want to add: '))
            print("Item added to cart")
            price = quantity * int(selected_item[1])
            main_list.append([selected_item[0], quantity, price])
        else:
            print("Invalid item. Please enter a valid item.")

    # Save the updated cart to the user's cart file
    save_cart(user_id, main_list)


# Function to load the user's shopping cart
def load_cart(user_id):
    try:
        with open(f'{user_id}_cart.txt', 'r') as file:
            # Read and parse the contents of the cart file
            return [
                list(map(eval, line.strip('[]').split(',')))
                for line in file.read().split('\n') if line
            ]
    except FileNotFoundError:
        # If the cart file is not found, create an empty cart
        with open(f'{user_id}_cart.txt', 'w') as file:
            return []


# Function to save the user's shopping cart
def save_cart(user_id, cart):
    with open(f'{user_id}_cart.txt', 'a') as file:
        # Write each item in the cart to the cart file
        for item in cart:
            file.write(f"{str(item)}\n")


# Function to load available items from the product list
def load_items():
    with open('product.txt', 'r') as file:
        # Read and parse the contents of the product file
        return [line.strip().split(':') for line in file]


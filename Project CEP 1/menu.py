# Importing necessary functions/classes from the respective modules
from Actions import *
from add_items_to_cart import add_items_to_cart
from view_cart import view_cart
from checkout import check_out
from product import view_menu
from user_history import read_user_history

# Function to perform shopping actions for a user
def perform_shopping_actions(user_id):
    while True:
        print("    ~~Main Menu~~")
        print(f'Hey! {user_id}, what do you want to do?')
        action = input(
            "1. View Menu\n"
            "2. Add to Cart\n"
            "3. View Cart\n"
            "4. Remove from Cart\n"
            "5. Checkout\n"
            "6. Logout\n"
            "7. View History\n"
            "--Enter the number corresponding to the action you want to perform-- \n"
        )

        if action == "1":
            view_menu(user_id)  # Display the menu of available products

        elif action == "2":
            add_items_to_cart(user_id)  # Add items to the user's shopping cart

        elif action == "3":
            view_cart(user_id)  # View the contents of the user's shopping cart

        elif action == "4":
            remove_from_cart(user_id)  # Remove items from the user's shopping cart

        elif action == "5":
            check_out(user_id)  # Proceed to checkout

            # Break the loop after checkout to exit the shopping session
            break

        elif action == "6":
            print("Logout Successful")
            break  # Break the loop to exit the shopping session

        elif action == "7":
            read_user_history(user_id)  # View the purchase history of the user

        else:
            print("Please Enter a valid number")

# Importing necessary functions/classes from accounts and menu modules
from accounts import create_account, login
from menu import perform_shopping_actions

# Asking the user whether they have an account or not
print("♥♥♥♥--WELCOME TO BEAUTY ICON--♥♥♥♥")
verification = input("Do you have an account? Enter the corresponding number \n1. Yes \n2. No\n")

# User input loop to handle account verification
while True:
    if verification == "1":
        user_id = input("---Enter Your USER ID:\n")
        user_id = login(user_id)  # Log in the user using the provided user ID
        break
    elif verification == "2":
        user_id = input("---Enter Your USER ID:\n").strip()
        create_account(user_id)  # Create a new account for the user using the provided user ID
        break
    else:
        print("--Please enter the correct number:\n")
        verification = input("Do you have an account? Enter the corresponding number \n 1. Yes \n2. No\n")
        continue

# Once the user is logged in or a new account is created, perform shopping actions
perform_shopping_actions(user_id)



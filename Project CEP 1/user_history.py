# Function to read and display the purchase history of a user
def read_user_history(user_id):
    try:
        # Try to open and read the user's history file
        with open(f'{user_id}.txt', 'r') as history_file:
            content = history_file.read()
            print(f"{user_id} Your History:\n {content}")
    except FileNotFoundError:
        # Handle the case where the user's history file does not exist
        print(f"User history file for {user_id} does not exist.")

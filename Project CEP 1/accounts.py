# Creating a history file to store user records
with open('history_of_users.txt', 'a') as file:
    pass

# Function to create a new user account
def create_account(user_id):
    # Check if user already exists in the history
    with open('history_of_users.txt', 'r') as file:
        # Read all user records from history
        user_records = [line.strip().split(",") for line in file]

    for record in user_records:
        if user_id == record[0]:  # Assuming user_id is the first element in each record
            print("User ID already exists")
            user_id = input("--Enter User_ID: \n")

    password = input("--Enter your password: \n").strip()

    # Create account
    with open(f'{user_id}.txt', 'w') as file:
        if len(password) >= 8 and any(char in "@#$%^&*!" for char in password) and any(num in '0123456789' for num in password):
            file.write(f'{user_id},{password}')

            # Take user's address as input
            address = input("--Enter your address : \n")
            num_in_add = any(num.isdigit() for num in address)
            while True:
                if num_in_add:
                    break
                elif not num_in_add:
                    print("!!Enter correct address!!")
                    address = input("Enter your address: ")
                    break

            # Take user's phone number as input
            while True:
                ph_no = input("Enter your phone number containing 11 digits: ")
                if len(ph_no) == 11:
                    print("~~Account Created Successfully~~")
                    break
                else:
                    print("Enter correct phone number!!")
                    continue

            # Append the new user record to history
            with open("history_of_users.txt", 'a') as history_file:
                history_file.write(f'{user_id},{password},{address},{ph_no}\n')
        else:
            print("!!!PASSWORD SHOULD CONTAIN:\n--minimum length of 8 characters\n--1 special character\n--1 digit!!!")

            create_account(user_id)


# Function to login
def login(user_id):
    password = input('Enter your password containing one special character and one number: \n').strip()
    while True:
        authentication = False

        # Check if user exists in history
        with open('history_of_users.txt', 'r') as file:
            # Read all user records from history
            user_records = [line.strip().split(",") for line in file]

            for record in user_records:
                if user_id == record[0] and password == record[1]:
                    print("~~Login Successfully~~")
                    authentication = True
                    break

            if not authentication:
                print("Invalid user ID or password")
                user_id = input("Enter your user ID: ").strip()
                password = input('Enter your password containing one special character and one number: \n').strip()
                continue
            else:
                break

    return user_id


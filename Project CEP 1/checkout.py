#Check out


from datetime import datetime, date, time
def check_out(user_id):
  from menu import perform_shopping_actions
  with open(f'{user_id}_cart.txt','r') as file:   #reading user_cart
    content=file.read()[:-1]
    total_bill=0

    list_strings = content.split('\n')

    if list_strings==['']:             #if cart file is empty
      print("There is nothing in your cart, go back and add some products in your cart")
      perform_shopping_actions(user_id)
    else:
        main_list=[]                  #all content save in main list
        for i in list_strings:
          list=eval(i)                #as list is save as an string in file

          main_list.extend([list])    #storing all item in main list
        for i in main_list:
            print("Item:" ,i[0],'\n',"Quantity:",i[1],'\n',"Price:",i[2])
            print("------------")
            total_bill+=int(i[2])       #calculating total_bill
        print("Your Total bill is:   " ,total_bill)
        with open(f'{user_id}.txt','a') as file:   #appending item purchased in user file
          for i in main_list:
            file.write(f'Item: {i[0]}, Quantity: {i[1]}, Price: {i[2]}\n')
          file.write("Total Bill: " + str(total_bill) + '\n')
          address=input("Enter your address: ")
          file.write("Address: " + address + '\n')
          current_datetime = datetime.now()
          file.write(str(current_datetime))
          file.write("-----------------------------------\n")
          print(current_datetime)

          print(f"♣♣--Your order will be deliver to your address: {address} in just one hour--♣♣")
    print("♠♠--Thank you for shopping with us--♠♠")
    print("♦♦--Your order is confirmed--♦♦")

    # Open the cart file in write mode to truncate its contents
    with open(f'{user_id}_cart.txt', 'w') as cart_file:
        cart_file.truncate()

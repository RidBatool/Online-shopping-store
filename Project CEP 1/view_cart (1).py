#Function to view cart

def view_cart(user_id):
  try:                     #checking that user cart file is exist otr not
      with open(f'{user_id}_cart.txt', 'r') as file:
          lines = file.readlines()

      if not lines:      #if cart file is empty
          print("---Your cart is empty---")
      else:
          for line in lines:
              b = line.strip().split(',')
              print("Item:  ", b[0], '\n', "Quantity:  ", b[1], '\n', "Price:  ", b[2])
              print("-----------------------------------")

  except FileNotFoundError:         #if file does not exist
      print("---Your cart file does not exist---")

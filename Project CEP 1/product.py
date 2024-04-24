#creating product available file
with open('product.txt', 'w') as file:
    file.write('Foundation:500\nConcealer:650\nEyeshadow:900\nMascara:700\nLipstick:300\nEyeliner:700\nBlusher:900\nLipgloss:500\nBronzer:500\nHighlighter:700')

def view_menu(user_id):
    with open('product.txt', 'r') as file:
         print(file.read())

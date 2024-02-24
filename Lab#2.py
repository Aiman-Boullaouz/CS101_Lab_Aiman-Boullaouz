########################################################################
##
## CS 101 Lab
## Program # 2
## Name: Aiman Boullaouz
##
########################################################################

#get user input
product = input('Enter the product name: ')
quantity = int(input('Enter the quantity purhcased: '))
unit_price = float(input('Enter the unit price of the product: '))

#declare discount
if quantity >= 50:
    discount_percentage = 15
elif 20 <= quantity < 50:
    discount_percentage = 10
elif 10 <= quantity < 20:
    discount_percentage = 5
else:
    discount_percentage = 0

#calculations
total_cost = quantity * unit_price

discount_amount = (discount_percentage / 100) * total_cost

dicounted_cost = total_cost - discount_amount

#output
print()
print('Invoice Summary:')
print(f'Prodcut: {product}')
print(f'Quantity: {quantity}')
print(f'Unit Price: ${unit_price}')
print(f'Total cost (Before Discount): ${total_cost:.2f}')
if discount_percentage > 0:
    print(f'Discount Applied: {discount_percentage}%')
    print(f'Discount Amount: ${discount_amount:.2f}')
print(f'Discounted Cost: ${dicounted_cost:.2f}')
      

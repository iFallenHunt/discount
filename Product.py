price = int(input('Inform the price of the product: '))
pdiscount = int(input('Inform the discount percentage: '))
vdiscount = int
ppay = int
vdiscount = price * pdiscount / 100
ppay = price - vdiscount
print('The amount to pay is: ', ppay)
print('The discount amount is: ', vdiscount)